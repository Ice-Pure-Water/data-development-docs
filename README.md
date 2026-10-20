# 数据方案 Markdown 转规格文档与 HTML

`data-development-docs` 将不同业务的方案 Markdown 按数据规格规则整理成结构统一、事实可追溯的规格 Markdown，再由该规格 Markdown 生成便于展示、讲解和逐层阅读的 HTML。业务事实、阶段数量、数据对象角色、适用范围和逻辑条目均从输入抽取，不预设固定案例。规格 Markdown 是内容基线；用户明确要求时，可再生成互相链接的完整规格 HTML。

产物包括规范化规格 Markdown 和方案主页 HTML。主页使用纵向主流程图，涵盖所有可独立讲解的业务逻辑、按“对象作用为行、适用范围为列”对齐展示的数据对象和字段血缘。对象区不用 HTML 表格或卡片。内容只描述方案，不呈现实现 SQL、测试验证、进度、部署运维或数据使用者说明。来源 Markdown 提供业务事实；DDL 仅用于说明结构。

工作步骤见 [SKILL.md](SKILL.md)，页面内容模型、三栏联动、逻辑专题、数据对象清单、血缘及电脑端宽屏规则见 [HTML 阅读与交互规范](references/html-reading-view.md)。流程图关系建模、正交路由和交叉处理见[内置流程图绘制方法](references/flow-diagram-method.md)；文字层级、中文排版、阅读节奏和展示检查见[内置文字展示方法](references/text-display-method.md)；中文表达原则见[文字与视觉设计准则](references/writing-and-visual-design.md)。两类方法均已融入本 skill。
