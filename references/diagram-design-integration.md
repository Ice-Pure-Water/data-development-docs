# diagram-design 来源与本 skill 的适配边界

流程图规范直接采用 [`cathrynlavery/diagram-design`](https://github.com/cathrynlavery/diagram-design/tree/f2f4d49ea8d632f17cf196ba26599277a93f767b/skills/diagram-design)，核对版本为 `f2f4d49ea8d632f17cf196ba26599277a93f767b`（插件版本 2.6.115，GitHub `main` 当前指向该提交）。上游仓库采用 MIT License，见[许可证](https://github.com/cathrynlavery/diagram-design/blob/f2f4d49ea8d632f17cf196ba26599277a93f767b/LICENSE)。

## 规范优先级

`diagram-design` 是数据规格图的规范来源。随本 skill 发布的[数据规格图执行规则](flow-diagram-method.md)只摘要上游方法并指出数据规格文档的适用图形，不另行替代或降低上游要求。发生描述差异时，以锁定提交中的上游 `SKILL.md`、`references/type-architecture.md`、`references/type-flowchart.md`、`references/primitives-core.md`、`references/style-guide.md`、`references/layout-budget.md` 和 `references/animation.md` 为准。

## 唯一图形例外

用户明确要求：主流程图的连接线不带箭头，数据流向由短线段沿每条真实数据连线连续流动表示，不用单个光点。此项明确覆盖上游 `animation.md` 对循环流动线段的限制；例外仅限无箭头方向提示和逐条连线的线段动效。图形类型选择、架构布局、节点和边预算、正交路由、桥接、配色、文字层级、可访问性及静态降级全部遵循 diagram-design。每条路径保留完整静态底线；减少动态效果或打印时隐藏动效线段但保留静态关系。

## 保留的页面与文档约束

下列约束来自用户对数据规格 HTML 的明确需求，作用于内容结构和页面交互，不构成另一套绘图规范：整体方案图优先纵向阅读；阶段导航、图中阶段、详情和读写对象联动；数据对象独立于流程图，按“对象作用为行、适用范围为列”分区；完整规格可单独成页；页面面向电脑端，整体图不可在内部横向拖动。图节点、连线、颜色、线型、字体、排布、交叉处理和动效仍执行上游规范。

源版本信息应在更新 diagram-design 插件后同步核对，避免本 skill 摘要与上游规范漂移。
