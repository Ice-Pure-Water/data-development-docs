# 数据开发文档与数据规格

`data-development-docs` 是一个用于编写和维护数据交付文档的 Codex skill。它把**数据开发方案**与**数据规格**合并在一份连贯的文档里，帮助业务、开发和测试读者从总体方案一路理解业务规则、数据处理过程和最终字段来源。

## 文档重点

按以下顺序组织内容，让读者先理解整体，再查阅细节：

1. **整体方案**：数据范围、来源、主要处理阶段和结果。
2. **业务规格**：数据粒度、主键、业务定义、纳入/排除条件、规则优先级、例外情况和待决口径。
3. **处理逻辑**：每个步骤的输入、输出、过滤、关联、转换、聚合、选择与合并方式。
4. **字段血缘**：结果字段对应的来源表字段、常量或计算规则，经过的处理步骤，以及空值、冲突和默认值处理。

数据表按角色梳理，覆盖**来源表、配置/字典表、核心/中间表和结果表**。涉及多个环境或阶段时，列明测试/开发阶段与正式阶段的数据库和完整表名，并区分当前 SQL 引用、DDL 目标和已确认的物理表。库表清单独立呈现，不塞进流程图节点。

## Markdown 与 HTML

- Markdown 是可编辑的事实源；需求规则、SQL、代码、配置和 DDL 是整理规格时的依据。
- 需要演示时，HTML 总览页优先展示主流程、关键业务规则、主要库表和重要字段路径；详细查阅可放在同套文档的独立完整页面。
- 流程图、侧边流程导航和正文细节相互定位：导航链接正文锚点，阅读细节时能看到当前流程阶段；有关联的图节点可跳转到同页说明。
- 流程线可以使用克制的流动点表达方向。节点文字需完整容纳，连线清晰且尽量不交叉；动画需支持系统的“减少动态效果”设置。
- HTML 标题介绍下方直接展示可点击的外部依据与参考链接，例如需求文档、规范或参考代码；保持为简洁的行内说明，不单独增加“参考资料/资源”区块。项目内 Markdown、SQL、DDL 等文件只在对应规格或处理逻辑处引用，不混入外部参考链接。
- 两种格式都要保持同一套业务事实、表名、字段名和规则口径。
- HTML 总览、完整 HTML 与 Markdown 按固定内容契约生成：业务规则说明触发条件、优先级、结果与依据；处理步骤说明输入、筛选关联、转换顺序、输出与边界；字段血缘逐字段列出来源、推导、处理位置和空值/冲突行为。详细字段见 `references/document-model.md` 与 `references/html-reading-view.md`。

## 写作约定

- 以自然、符合业务上下文的中文表达概念，不把英文术语逐字硬译；库名、表名、字段名和代码标识保持准确。
- 清楚区分已确认的业务要求、当前代码/DDL 行为、目标设计和待决事项。
- 使用实际业务名称和技术标识，不编造可见的规则编号或对象代号。
- 默认不加入测试方案或结果、验证结论、进度、验收、发布、运维或面向数据使用者的说明。用户明确要求时再扩展。

## 使用方式

```text
使用 $data-development-docs，基于需求、SQL/代码、配置和 DDL，
整理这项数据交付物的整体方案、业务规格、处理逻辑和字段血缘。
列清来源表、配置表、核心表和结果表；如果涉及不同阶段，列明各阶段的数据库及完整表名，
并标明 SQL 引用、DDL 目标或已确认物理表。区分已确认规则、当前实现、目标设计和待决事项。
需要演示时再生成 HTML 总览页，并让流程、侧边导航与正文细节联动。
```

## Skill 文件

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── data-contracts.md
│   ├── document-model.md
│   ├── html-reading-view.md
│   └── lineage-and-implementation.md
└── templates/
    └── data-development-specification.md
```

## 参考思想

内容组织借鉴 Diátaxis 的读者任务分类与 arc42 的方案视角。数据关系和字段血缘参考 [dbt 项目血缘](https://docs.getdbt.com/docs/explore/explore-projects)、[DataHub 数据血缘](https://docs.datahub.com/docs/features/feature-guides/lineage) 和 [OpenMetadata 字段级血缘](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-lineage/column)。流程图布局按需采用 Graphviz 的分层思路或 ELK 的正交连线能力；HTML 设计参考 Effective HTML、Huashu Design、frontend-design 和 diagram-design 的适用方向，但以规格文档的阅读任务为准，不照搬某个工具的页面样式。

中文表达参考 [leter/zh-tech-writing](https://github.com/leter/zh-tech-writing)，并根据具体业务维护一致的术语选择。
