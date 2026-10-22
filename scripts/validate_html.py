#!/usr/bin/env python3
"""Check that a generated presentation HTML still uses the canonical template."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from html.parser import HTMLParser
from pathlib import Path


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.styles: list[str] = []
        self.scripts: list[str] = []
        self.placeholders: list[str] = []
        self.stage_keys: dict[str, list[str]] = {
            "data-stage-link": [],
            "data-stage-marker": [],
            "data-stage-detail": [],
            "data-stage-node": [],
            "data-stage-band": [],
        }
        self.flow_edges = 0
        self.flow_motion = 0
        self.flow_nodes: list[dict[str, str]] = []
        self.flow_motion_nodes: list[dict[str, str]] = []
        self.flow_viewboxes: list[str] = []
        self.flow_has_arrowhead = False
        self.grid_scope_count: int | None = None
        self.has_object_grid = False
        self.grid_cell_count = 0
        self.grid_rows: list[int] = []
        self._element_stack: list[tuple[str, dict[str, str]]] = []
        self._style_depth = 0
        self._script_depth = 0
        self._style_content: list[str] = []
        self._script_content: list[str] = []
        self._in_flow_canvas = 0
        self._in_object_grid = 0
        self._in_grid_row = 0
        self._current_grid_row_cells = 0
        self.inline_styles: list[tuple[str, str]] = []
        self.external_resources: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        self._element_stack.append((tag, values))
        classes = set(values.get("class", "").split())
        if values.get("id"):
            self.ids.append(values["id"])
        if values.get("href"):
            self.hrefs.append(values["href"])
        if (tag == "script" and values.get("src")) or (tag == "link" and "stylesheet" in values.get("rel", "").lower().split()):
            self.external_resources.append(tag)
        if "style" in values:
            self.inline_styles.append((values.get("class", ""), values["style"]))
        for key in self.stage_keys:
            if values.get(key):
                self.stage_keys[key].append(values[key])
        if "data-flow-edge" in values:
            self.flow_edges += 1
        if "data-flow-motion" in values:
            self.flow_motion += 1
            self.flow_motion_nodes.append(values)
        if "data-stage-node" in values:
            self.flow_nodes.append(values)
        if tag == "style":
            self._style_depth += 1
        if tag == "script":
            self._script_depth += 1
        if "flow-canvas" in classes:
            self._in_flow_canvas += 1
        if tag == "svg" and self._in_flow_canvas:
            self.flow_viewboxes.append(values.get("viewbox", ""))
        if self._in_flow_canvas and "marker-end" in values:
            self.flow_has_arrowhead = True
        if "object-grid" in classes:
            self._in_object_grid += 1
            self.has_object_grid = values.get("role") == "table"
            match = re.fullmatch(r"--scope-count:\s*(\d+)\s*", values.get("style", ""))
            if match:
                self.grid_scope_count = int(match.group(1))
        if self._in_object_grid and values.get("role") == "row":
            self._in_grid_row += 1
            self._current_grid_row_cells = 0
        if self._in_object_grid and values.get("role") in {"columnheader", "rowheader", "cell"}:
            self.grid_cell_count += 1
            if self._in_grid_row:
                self._current_grid_row_cells += 1

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_data(self, data: str) -> None:
        if self._style_depth:
            self._style_content.append(data)
        if self._script_depth:
            self._script_content.append(data)

    def handle_comment(self, data: str) -> None:
        if "{{" in data or re.search(r"\b(?:NAV_LINKS|SOURCE_LINKS|STAGE_LINKS|FLOW_SVG|PHASE_DETAILS|STAGE_MARKERS|LOGIC_INTRO|LOGIC_ITEMS|SCOPE_COUNT|OBJECT_GRID_ROWS|LINEAGE_INTRO|LINEAGE_TABLE|SOURCE_NOTES)\b", data):
            self.placeholders.append(data.strip())

    def handle_endtag(self, tag: str) -> None:
        if tag == "style" and self._style_depth:
            self._style_depth -= 1
            self.styles.append("".join(self._style_content))
            self._style_content = []
        if tag == "script" and self._script_depth:
            self._script_depth -= 1
            self.scripts.append("".join(self._script_content))
            self._script_content = []
        if not self._element_stack:
            return
        # HTMLParser is tolerant of void tags; unwind through the matching node.
        for index in range(len(self._element_stack) - 1, -1, -1):
            if self._element_stack[index][0] == tag:
                removed = self._element_stack[index:]
                del self._element_stack[index:]
                for _, values in reversed(removed):
                    classes = set(values.get("class", "").split())
                    if "flow-canvas" in classes:
                        self._in_flow_canvas -= 1
                    if "object-grid" in classes:
                        self._in_object_grid -= 1
                    if self._in_object_grid and values.get("role") == "row":
                        self.grid_rows.append(self._current_grid_row_cells)
                        self._in_grid_row -= 1
                break


def extract_template_blocks(path: Path) -> tuple[str, str]:
    parser = DocumentParser()
    parser.feed(path.read_text(encoding="utf-8"))
    parser.close()
    if len(parser.styles) != 1 or len(parser.scripts) != 1:
        raise ValueError(f"模板应恰有一个 style 和一个 script 块：{path}")
    return parser.styles[0], parser.scripts[0]


def validate(html_path: Path, template_path: Path, diagram_self_check: Path | None = None) -> list[str]:
    errors: list[str] = []
    source = html_path.read_text(encoding="utf-8")
    parser = DocumentParser()
    parser.feed(source)
    parser.close()

    template_style, template_script = extract_template_blocks(template_path)
    if parser.styles != [template_style]:
        errors.append("页面 CSS 与标准模板不一致，检查是否改了主题、字号、间距或组件样式。")
    if parser.scripts != [template_script]:
        errors.append("页面交互脚本与标准模板不一致。")
    if re.search(r"\{\{[A-Z0-9_]+\}\}", source):
        errors.append("页面仍有未替换的模板占位符。")
    if parser.placeholders:
        errors.append("页面仍有未替换的模板插槽注释。")
    if parser.external_resources:
        errors.append("页面引入外部 CSS 或 JavaScript，离线页面应只用内嵌资源。")
    if len(parser.ids) != len(set(parser.ids)):
        errors.append("页面存在重复 id。")
    required_ids = ["top", "main", "journey", "logic", "objects", "lineage", "source-notes"]
    if not all(ident in parser.ids for ident in required_ids):
        errors.append("主页缺少固定结构区。")
    else:
        positions = [parser.ids.index(ident) for ident in required_ids]
        if positions != sorted(positions):
            errors.append("主页固定内容区顺序偏离标准模板。")
    id_set = set(parser.ids)
    if any(href.startswith("#") and href[1:] not in id_set for href in parser.hrefs):
        errors.append("页面内导航链接指向不存在的锚点。")
    if (len(parser.inline_styles) != 1
            or "object-grid" not in parser.inline_styles[0][0].split()
            or not re.fullmatch(r"--scope-count:\s*\d+\s*", parser.inline_styles[0][1])):
        errors.append("页面有额外 inline 样式；只允许对象矩阵的动态范围列数。")
    if not parser.has_object_grid:
        errors.append("对象矩阵缺少 role=table 容器。")
    if parser.grid_scope_count is None or parser.grid_scope_count < 1:
        errors.append("对象矩阵缺少有效的 --scope-count。")
    elif any(count != parser.grid_scope_count + 1 for count in parser.grid_rows):
        errors.append("对象矩阵各行单元格数量与适用范围列数不一致。")
    if not parser.grid_rows:
        errors.append("对象矩阵没有语义化的 role=row 行。")

    keys = {name: set(values) for name, values in parser.stage_keys.items()}
    nav_keys = keys["data-stage-link"]
    if not nav_keys:
        errors.append("没有阶段导航项。")
    if len(parser.stage_keys["data-stage-link"]) != len(nav_keys):
        errors.append("阶段导航键重复。")
    for name in ("data-stage-marker", "data-stage-detail"):
        values = parser.stage_keys[name]
        if len(values) != len(set(values)) or set(values) != nav_keys:
            errors.append(f"{name} 与阶段导航键不一一对应。")
    for name in ("data-stage-node", "data-stage-band"):
        if keys[name] != nav_keys:
            errors.append(f"{name} 与阶段导航键不一致。")
    for node in parser.flow_nodes:
        if node.get("tabindex") != "0" or node.get("role") != "button" or not node.get("aria-label"):
            errors.append("每个可交互流程节点都需 tabindex=0、role=button 和 aria-label。")
            break
    for motion in parser.flow_motion_nodes:
        if motion.get("aria-hidden") != "true" or motion.get("focusable") != "false":
            errors.append("流动线段属于装饰层，需从辅助技术焦点中隐藏。")
            break

    if parser.flow_edges != parser.flow_motion:
        errors.append("静态数据连线与流动短线数量不一致。")
    if parser.flow_edges == 0:
        errors.append("主流程图没有带 data-flow-edge 的静态连线。")
    if parser.flow_has_arrowhead:
        errors.append("主流程图检测到箭头标记；数据方向应由流动线段表达。")
    if not parser.flow_viewboxes:
        errors.append("主流程区没有内嵌 SVG。")
    elif any(not re.fullmatch(r"0\s+0\s+960\s+\d+(?:\.\d+)?", box) for box in parser.flow_viewboxes):
        errors.append("流程图 SVG 的 viewBox 宽度应固定为 960。")
    if diagram_self_check:
        flow_region = re.search(r'<div class="flow-canvas">(.*?)</div>', source, re.S)
        svg_match = re.search(r"<svg\b.*?</svg>", flow_region.group(1), re.S | re.I) if flow_region else None
        if not svg_match:
            errors.append("无法从主流程区提取 SVG 交给 diagram-design self-check。")
        else:
            wrapper = f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><style>{template_style}</style></head><body><div class="flow-canvas">{svg_match.group(0)}</div></body></html>'
            temp_path: Path | None = None
            try:
                with tempfile.NamedTemporaryFile("w", suffix=".html", encoding="utf-8", delete=False) as temp_file:
                    temp_file.write(wrapper)
                    temp_path = Path(temp_file.name)
                result = subprocess.run(
                    [sys.executable, str(diagram_self_check), "--offline", str(temp_path)],
                    capture_output=True, text=True, check=False,
                )
                if result.returncode:
                    details = (result.stdout + result.stderr).strip()
                    errors.append(f"diagram-design SVG self-check 失败：{details}")
            except OSError as exc:
                errors.append(f"无法运行 diagram-design SVG self-check：{exc}")
            finally:
                if temp_path:
                    temp_path.unlink(missing_ok=True)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path, help="生成的主页 HTML")
    parser.add_argument("--template", type=Path, default=Path(__file__).resolve().parents[1] / "assets/html-page-template.html")
    parser.add_argument("--diagram-self-check", type=Path, help="已安装 diagram-design skill 的 scripts/self_check.py")
    args = parser.parse_args()
    errors = validate(args.html, args.template, args.diagram_self_check)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"HTML 结构和样式与标准模板一致：{args.html}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
