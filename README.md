# 数据开发文档与数据规格 Skill

`data-development-docs` 用于维护一份统一的数据开发文档与数据规格，核心顺序是整体方案、业务规格、处理逻辑、字段血缘。文档要列清来源表、配置/字典表、核心/中间表和结果表；涉及多个阶段时，按测试/开发阶段和正式阶段列出数据库与完整表名，并注明它来自当前 SQL、目标 DDL 还是已确认的物理结构。库表清单独立于流程图。

Markdown 是可编辑事实源。HTML 演示页优先展示主流程、关键业务规格、主要库表和关键字段路径；流程图和明细通过侧边流程导航与正文锚点联动，阅读细节时仍能定位整体流程。详细规则和字段说明可以放在同一套文档中的独立完整文档页。流程动效可参考沿连线移动的流动点，但应少量、克制、按实际路径着色，并支持减少动态效果。图中标签需完整落在节点内，连线尽量不交叉。

术语按业务上下文选择自然中文表达，不把英文名词逐字硬译；真实库名、表名、字段名和代码标识保持原样。文档服务业务、开发、测试读者理解规格，不默认扩展成面向数据使用者的说明，也不加入测试方案/结果、验证、进度、验收、发布或运维章节。

## 调用示例

```text
使用 $data-development-docs，基于需求、SQL/代码和 DDL，
为这个数据交付物整理整体方案、业务规格、处理逻辑和字段血缘。
区分已确认规则、当前实现和待决事项；输出 Markdown。
需要演示页时，在一个连续页面展示主流程、关键规格、来源/配置/核心/结果表和主要字段路径；库表单独成块，并区分测试/开发阶段与正式阶段。用侧边流程导航联动正文锚点；细节可放在独立完整文档页。不要加入测试方案/结果、验证、进度或数据使用者说明。
```

## 文件结构

```text
.
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── document-model.md
│   ├── data-contracts.md
│   ├── lineage-and-implementation.md
│   └── html-reading-view.md
└── templates/data-development-specification.md
```

## 思想来源

内容结构借鉴 Diátaxis 的读者任务分类、arc42 的上下文/方案/构件视角，以及 [dbt 项目血缘](https://docs.getdbt.com/docs/explore/explore-projects)、[DataHub 数据血缘](https://docs.datahub.com/docs/features/feature-guides/lineage) 和 [OpenMetadata 字段级血缘](https://docs.open-metadata.org/v1.12.x/how-to-guides/data-lineage/column) 中的来源与字段关系表达。流程图布局参考 Graphviz 分层布局和 ELK 正交连线的适用场景。HTML 设计流程参考 Effective HTML 的按任务选型思路，并将 Huashu Design、frontend-design、diagram-design 作为按需比较的视觉方案，不把任何一个框架的页面样式直接套进规格文档。

中文技术写作参考 [leter/zh-tech-writing](https://github.com/leter/zh-tech-writing) 的简洁、平实表达原则；本 Skill 额外要求按领域语境选词，并维护项目自己的术语表，避免通用写作规范替代业务定义。
