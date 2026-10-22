---
name: data-development-docs
description: Turn existing data proposal Markdown into a traceable data specification Markdown and a coordinated presentation HTML. Use when restructuring data plans or generating their specification view. Does not implement data processing.
metadata:
  short-description: Convert data proposals into specifications and presentation HTML
---

# 数据方案转规格文档与 HTML

把一份或多份方案 Markdown 整理成统一、可追溯的数据规格 Markdown，再从该 Markdown 生成展示型 HTML。面向不同业务，不预设阶段、表、字段、环境或规则数量。

## 工作步骤

1. 确定输入方案 Markdown、用户提供的规格规则/模板、规格 Markdown 和 HTML 的输出位置。只读取来源明确引用的需求材料；需要说明结构时可读取相关 DDL。
2. 抽取目标、数据流、阶段、读写关系、所有可独立讲解的业务判断、数据对象、字段血缘、术语、链接、冲突和未决事项。记录重要事实的来源位置。
3. 先生成规格 Markdown，再从它生成 HTML。用户提供的规格规则优先；否则按[内容与 HTML 规范](references/content-and-html.md)。Markdown 是事实基线，HTML 不作为编辑源。
4. 生成 HTML 时，必须以[标准页面模板](assets/html-page-template.html)为唯一页面骨架，按[HTML 内容与稳定性约定](references/content-and-html.md)填充；不得为不同项目另选主题或改成另一种页面布局。中文文字按[中文写作与展示规范](references/chinese-writing-and-display.md)组织，流程图按[diagram-design 规则与来源](references/diagram-design.md)绘制。
5. 按稳定性约定逐项核对生成结构、内容清单、对象范围矩阵和来源链接。此项只检查 Markdown 到 HTML 的呈现一致性，不验证 SQL、数据库或业务结果。

## 范围

- 只描述数据方案和规格。逻辑写方案，不写实现 SQL；可引用已有或设计中的 DDL 说明结构。
- 不纳入实现 SQL 内容/文件清单、测试与验证、进度、运行或部署状态、发布运维、数据使用者说明。
- 不把推测写成事实。冲突并列标“待确认”；DDL 不代表对象已部署。
- 中文术语按业务语境选择并全文一致；技术标识、字段名、库表名、代码值和专名保留原文。
- HTML 默认是自包含的电脑端讲解主页。只有用户明确要求时，才另生成互链的完整规格 HTML。
