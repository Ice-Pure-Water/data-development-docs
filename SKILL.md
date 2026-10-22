---
name: data-development-docs
description: Turn existing data proposal Markdown into a traceable data specification Markdown and a coordinated presentation HTML. Use when restructuring data plans or generating their specification view. Does not implement data processing.
metadata:
  short-description: Convert data proposals into specifications and presentation HTML
---

# 数据方案转规格文档与 HTML

把一份或多份方案 Markdown 整理成统一、可追溯的数据规格 Markdown，再从该 Markdown 生成展示型 HTML。面向不同业务，不预设阶段、表、字段、环境或规则数量。

## 工作步骤

1. 确定输入方案 Markdown、用户提供的 Markdown 规格规则/模板、规格 Markdown 和 HTML 的输出位置。只读取来源明确引用的需求材料；需要说明结构时可读取相关 DDL。
2. 抽取目标、数据流、阶段、读写关系、所有可独立讲解的业务判断、数据对象、字段血缘、术语、链接、冲突和未决事项。记录重要事实的来源位置。
3. 先生成规格 Markdown，再从它生成 HTML。用户提供的规格格式只决定 Markdown 的内容组织；HTML 按[内容与 HTML 规范](references/content-and-html.md)转换。Markdown 是事实基线，HTML 不作为编辑源。
4. 生成 HTML 时，必须以[标准页面模板](assets/html-page-template.html)为唯一主页骨架，按[HTML 内容与稳定性约定](references/content-and-html.md)填充；不同项目共用同一页面和流程图 profile。中文文字按[中文写作与展示规范](references/chinese-writing-and-display.md)组织；绘制流程图前调用安装的 diagram-design skill，并按[数据规格场景规则](references/diagram-design.md)适配。
5. 运行 `python3 scripts/validate_html.py --diagram-self-check <diagram-design-skill>/scripts/self_check.py <主页.html>`。该检查器会抽出主流程 SVG 单独交给上游 self-check，避免主页面阶段联动脚本干扰检查；再按 diagram-design 几何规则检查交叉、重叠和文字越界。修复所有呈现偏差后再交付；不验证 SQL、数据库或业务结果。

## 范围

- 只描述数据方案和规格。逻辑写方案，不写实现 SQL；可引用已有或设计中的 DDL 说明结构。
- 不纳入实现 SQL 内容/文件清单、测试与验证、进度、运行或部署状态、发布运维、数据使用者说明。
- 不把推测写成事实。冲突并列标“待确认”；DDL 不代表对象已部署。
- 中文术语按业务语境选择并全文一致；技术标识、字段名、库表名、代码值和专名保留原文。
- HTML 默认是自包含的电脑端讲解主页。只有用户明确要求时，才另生成互链的完整规格 HTML。
