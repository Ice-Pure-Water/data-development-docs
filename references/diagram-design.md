# 流程图规则与来源

流程图设计遵循上游 [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)。本技能锁定来源提交 `f2f4d49ea8d632f17cf196ba26599277a93f767b`（MIT）；细节以该版本的 `SKILL.md` 及架构、流程图、布局、样式和动效参考为准。本文件只规定数据规格场景的选型和适配，不另造一套绘图规范。

## 执行约定

- 绘制前调用已安装的 `diagram-design` skill，并读取其 `SKILL.md`、Architecture 类型、布局预算、style guide、输出尺寸、简体中文及动画参考。主数据流程固定采用 Architecture、纵向主轴和浅色主题；节点拓扑来自规格 Markdown，不从其他项目 HTML 复制。上游规则是绘图规范的来源；本文件和页面模板只锁定数据规格场景的参数。
- `assets/html-page-template.html` 中的 `--diagram-*` 变量是所有项目共用的浅色 profile，也是 diagram-design 主题 onboarding 的已确认配置。始终使用该 profile，不为每个项目另选明暗主题、品牌色、字体、尺寸预设或视觉风格。数据规格主页必须离线可读，因此图中文字使用模板的本地中文字体栈。
- 主图的 SVG 画布固定 `viewBox` 宽度为 `960` 个用户单位，高度按拓扑增加；CSS 最大显示宽度为 `960px`。主节点中文名使用 `20px`，次级说明 `16px`；超长文本换行或扩展节点高度，不缩小字号。图在固定中栏纵向滚动，禁止横向滚动和裁切。节点数量超过上游 Architecture 复杂度预算时，合并为准确的阶段概览节点，并把完整处理过程保留在对应阶段详情；不得压缩间距或字号塞入一张图。
- 统一映射上游语义色：普通处理节点使用 `--diagram-paper` 与 `--diagram-ink`；输入节点用 `--diagram-input-fill`、`--diagram-soft`；外部节点用 `--diagram-external-fill`、`--diagram-muted`；存储节点用 `--diagram-store-fill`、`--diagram-muted`；重点节点用 `--diagram-accent-tint`、`--diagram-accent`。普通数据连线使用 `--diagram-flow-line`，外部交互可用 `--diagram-link`。静态连线带 `data-flow-edge`，动效叠线带 `data-flow-motion`。SVG 只引用模板语义变量，不写项目私有色值或 inline 覆盖样式。
- 主流程每条有向数据关系绘制同一路径的静态底线（2px）和动效叠线（2.6px，`stroke-dasharray="12 20"`，`0.9s linear` 循环），叠线使用 `--diagram-flow-motion`。连线无箭头；方向由连续移动的短线段表示，不使用单个光点。动效只沿既定路径移动，不改变拓扑、节点位置或文字。此为用户确认的数据流程动效约定，对上游箭头及动画默认值的窄范围覆盖；其余布局、路由、间距、复杂度、语义和可访问性规范仍执行上游要求。
- 主流程按上游正交布线，先处理分支、汇合、端口和交叉，再增加动效。每条关系保留完整静态底线，动效不掩盖底线。减少动态效果和打印时停用动效；静态关系仍完整可读。
- 每个 SVG 阶段底色使用 `data-stage-band`，节点使用 `data-stage-node`，阶段导航、正文标记和详情分别使用 `data-stage-link`、`data-stage-marker`、`data-stage-detail`；属性值全部引用同一阶段键。切换阶段时导航滚动到当前项、主图滚动到当前节点、右侧详情回到顶部，避免阶段已经变化而对应内容仍停在视口外。
- 中文节点文字按最终显示尺寸检查，扩框或换行，不得溢出。HTML 应有图标题、图意说明、键盘可达的节点交互及 `prefers-reduced-motion` 支持；动效元素标记 `data-flow-motion`，以便模板在减少动态效果时停用。当前阶段强调仅使用浅蓝背景与外框描边，不使用阴影、发光或改变其他节点颜色。

## 来源维护

上游来源和版本变更时，先核对许可证及固定提交，再更新本文件和主 skill 的调用指引。当前上游许可证：[MIT License](https://github.com/cathrynlavery/diagram-design/blob/f2f4d49ea8d632f17cf196ba26599277a93f767b/LICENSE)。
