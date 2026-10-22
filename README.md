# 数据方案转规格文档与 HTML

`data-development-docs` 将已有的一份或多份数据方案 Markdown，整理为统一、可追溯的数据规格 Markdown，再从规格 Markdown 生成适合讲解和逐层阅读的 HTML。

它关注业务方案、数据流、处理规则、库表对象和字段血缘。它不实现数据处理，也不把某个项目的表名、阶段、环境或业务规则写成通用模板。

## 适用场景

- 多份方案 Markdown 需要合并、去重并整理为数据规格。
- 已有规格 Markdown 需要转成结构一致、与文档内容联动的展示型 HTML。
- 需要集中阅读整体数据流、阶段处理、关键业务规则、数据对象和字段来源。

## 输入与产物

**输入**：方案 Markdown；可选的规格模板或规则文件、需求文档、参考资料、DDL。只读取输入明确引用的材料；DDL 用于说明声明结构，不代表数据库当前状态。

**产物**：

1. **规范化规格 Markdown**：记录方案目标、数据流、阶段处理、业务规则、数据对象、字段血缘、来源和未决口径。它是唯一内容基线。
2. **讲解主页 HTML**：默认生成自包含、离线可读的电脑端页面。用户明确要求时，再从同一规格 Markdown 生成与主页互链的完整规格 HTML。

## 页面组织

主页按以下顺序组织：

1. 业务标题与方案摘要；需求文档和外部参考链接紧随其下。
2. **整体流程讲解**：左侧阶段导航、中间纵向数据流程图、右侧当前阶段详情和读写对象。滚动、点击阶段或点击图节点时，三处保持联动。
3. **关键业务逻辑**：所有可单独讲解的判断分别列出，标题和摘要常显，细节在当前页面展开。
4. **数据对象**：按“对象作用为行、适用范围为列”对齐展示。库名、完整表名、用途和范围说清楚；对象区独立于流程图，不做卡片或 HTML 表格。
5. **字段血缘**：按目标字段说明含义、来源、推导规则、处理阶段和已知边界。
6. **方案来源**：保留可点击的来源 Markdown、需求资料和相关 DDL 链接。

业务阶段、主图区域、阶段详情和读写对象由同一内容清单生成；每条关系和逻辑都能回溯到规格 Markdown。所有项目复用同一页面骨架和视觉变量：[标准 HTML 模板](assets/html-page-template.html)。具体内容结构、固定样式和输出结构检查见[内容与 HTML 规范](references/content-and-html.md)。

## 生成原则

- 先整理规格 Markdown，再生成 HTML；不直接从零拼装 HTML。用户提供的格式或规则优先于默认结构。
- 以来源为依据。重要事实保留出处；重复事实去重；来源冲突或缺少口径时明确列出，不自行选定。
- 数据对象的角色与适用范围从输入提取，不预设“来源/配置/中间/结果”或“正式/测试”的固定集合。
- 术语按业务上下文使用自然中文。技术标识、库表字段名、代码值及专名保留原文。
- 主流程使用无箭头连线，以沿每条数据关系流动的短线段表达方向；静态路径始终完整可读。详细绘图来源和适配要求见[diagram-design 规则](references/diagram-design.md)。
- 中文层级、排版与阅读规则见[中文写作与展示规范](references/chinese-writing-and-display.md)。
- 不因业务国家或输入文档改换页面主题、栏目顺序或对象呈现方式；仅页面内容和依据 diagram-design 绘制的流程图拓扑随项目变化。

## 范围边界

本 skill 只整理和展示数据方案规格。逻辑只写方案，不写实现 SQL。可以链接已有或设计中的 DDL，但不据此声称对象已部署。

页面不包含实现 SQL 内容或文件清单、测试/验证、进度、运行与部署状态、发布运维、数据使用者说明。转换核对仅检查规格 Markdown 与 HTML 是否一致，不验证 SQL、数据库或业务结果。

## 安装与调用

将仓库克隆到 Codex skills 目录：

```bash
git clone https://github.com/Ice-Pure-Water/data-development-docs.git ~/.codex/skills/data-development-docs
```

安装后在 Codex 中调用 `$data-development-docs`，并提供源 Markdown、输出位置及适用的规格规则。例如：

> 使用 `$data-development-docs`，把 `方案A.md` 和 `方案B.md` 整理成数据规格 Markdown，并从该规格生成讲解型 HTML。输出到 `docs/`；保留来源链接和未决口径。

技能主流程见 [SKILL.md](SKILL.md)。

## 方法来源

本 skill 采用以下公开方法中与本任务相关的部分；业务事实仍只取自用户提供的材料，不复制来源项目的业务内容或页面模板。

| 来源 | 在本 skill 中的用途 |
| --- | --- |
| [diagram-design](https://github.com/cathrynlavery/diagram-design) | 架构图选型、拓扑、正交布线、样式和动效；按锁定版本执行，具体来源与数据规格适配见[图形规则](references/diagram-design.md)。 |
| [zh-tech-writing](https://github.com/leter/zh-tech-writing) | 自然中文、短句、术语一致和技术表达。 |
| [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | 根据主题和讲解场景确定视觉方向，减少模板化设计。 |
| [Effective HTML](https://github.com/plannotator/effective-html) 与 [Huashu Design](https://github.com/alchaincyf/huashu-design) | 内容优先、真实材料驱动排版和展示阅读方式的参考。 |
| [MDN Semantic HTML](https://developer.mozilla.org/en-US/curriculum/core/semantic-html/) 与 [MDN HTML Accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML) | 语义结构、键盘访问和内容可访问性。 |

diagram-design 的固定提交和 MIT 许可证见[图形规则](references/diagram-design.md)。其他链接用于说明方法出处；适用边界以本仓库的 skill 说明为准。
