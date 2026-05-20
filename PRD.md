# DocTransformer - 产品方案

## 1. 产品概述

### 产品名称
DocTransformer（文档转换器）

### 产品定位
让 AI Agent（Claude Code、Cursor 等）能够直接识别、编辑 Word/PDF 文档，并支持飞书、腾讯文档等在线协作平台的工具链。

### 核心价值
**把"上传-复制-粘贴"的低效流程，变成"直接编辑"的高效工作流。**

### 三种工作流
| 工作流 | 适用场景 | 命令 | 状态 |
|--------|----------|------|------|
| **工作流 A：转换编辑** | 本地 Word 文件，内容需要大改 | `dt convert` → 编辑 → `dt export` | MVP |
| **工作流 B：直接改格式** | 本地 Word 文件，内容已定，只调格式 | `dt format` | MVP |
| **工作流 C：在线文档集成** | 飞书/腾讯文档等在线协作平台 | `dt pull` / `dt push` | 扩展 |

---

## 2. 用户痛点

### 当前困境

| 场景 | 现状 | 问题 |
|------|------|------|
| **ChatGPT/Gemini** | 可以上传 Word/PDF | 修改后需要手动复制回去，格式可能丢失 |
| **Claude Code/Cursor** | 可以直接编辑 Markdown | 无法识别 Word/PDF，需要手动转换 |
| **公众号推文** | 初稿在 Word 中 | 需要在多个工具间来回切换 |
| **毕业论文** | 格式要求严格 | 修改内容容易，修改格式麻烦 |
| **飞书/腾讯文档** | 公司内部文档在云端 | 需要复制到本地编辑，再复制回去，流程繁琐 |

### 典型用户场景

**场景 1：公众号推文优化（工作流 A）**
```
当前流程：
Word初稿 → 复制到ChatGPT → 获取修改建议 → 手动粘贴回Word → 调整格式

理想流程：
Word初稿 → 转换为Markdown → Claude Code直接编辑 → 转换回Word → 完成
```

**场景 2：毕业论文 - 内容编辑（工作流 A）**
```
当前流程：
论文.docx → 复制内容到AI → 获取修改建议 → 手动粘贴回Word → 检查格式

理想流程：
论文.docx → 转换为Markdown → Claude Code编辑内容 → 使用模板导出Word → 格式自动符合要求
```

**场景 3：毕业论文 - 格式调整（工作流 B）**
```
当前流程：
内容已定 → 手动调整每个段落的字体、字号、行距 → 检查页边距 → 反复调整

理想流程：
内容已定 → dt format paper.docx --template thesis_cn → 一键完成所有格式调整
```

**场景 4：飞书/腾讯文档协作（工作流 C - 扩展功能）**
```
当前流程：
飞书文档 → 复制内容到AI → 获取修改建议 → 手动粘贴回飞书 → 检查格式

理想流程：
dt pull feishu://docx/xxx123 → Claude Code编辑 → dt push ./doc.md feishu://docx/xxx123
```

---

## 3. 产品功能

### 3.1 核心功能

#### F1: 文档转换（双向）
- **Word → Markdown**
  - 保留标题层级（H1-H6）
  - 保留加粗、斜体、删除线
  - 保留有序/无序列表
  - 保留表格
  - 保留图片（提取到单独文件夹）
  - 保留链接

- **Markdown → Word**
  - 使用模板保持格式一致
  - 支持自定义样式模板
  - 自动应用学校/公司格式要求

#### F2: 格式模板系统
- **内置模板**
  - 毕业论文模板（中文/英文）
  - 简历模板
  - 商务报告模板
  - 公众号文章模板

- **自定义模板**
  - 用户可上传自己的 .docx 作为模板
  - 保存为可复用模板

#### F3: 一键工作流
```bash
# 工作流 A：转换编辑（内容需要大改）
dt convert input.docx                    # 转换为 Markdown
# ... 在 Claude Code 中编辑 input.md ...
dt export input.md --template thesis     # 转换回 Word

# 工作流 B：直接改格式（内容已定，只调格式）
dt format input.docx --font "宋体" --size 12
dt format input.docx --template thesis_cn
```

#### F4: 直接修改格式（新增）
**适用场景**：内容已确定，只需要调整格式

- **段落样式**
  - 标题层级（H1-H6）
  - 对齐方式（左对齐、居中、右对齐）
  - 行距、段前段后间距
  - 首行缩进

- **字体设置**
  - 字体（宋体、黑体、Times New Roman 等）
  - 字号（小四、五号、12pt 等）
  - 颜色、加粗、斜体

- **页面设置**
  - 页边距（上下左右）
  - 纸张大小（A4、Letter 等）
  - 页眉页脚
  - 页码

- **其他格式**
  - 目录生成
  - 项目符号和编号
  - 表格格式

```bash
# 基本格式修改
dt format paper.docx --font "宋体" --size 12
dt format paper.docx --heading-font "黑体" --heading-size 16
dt format paper.docx --line-spacing 1.5
dt format paper.docx --margin-top 2.54cm --margin-bottom 2.54cm

# 使用模板批量修改格式
dt format paper.docx --template thesis_cn

# 组合修改
dt format paper.docx \
  --font "宋体" --size 12 \
  --heading-font "黑体" --heading-size 16 \
  --line-spacing 1.5 \
  --margin-top 2.54cm --margin-bottom 2.54cm
```

### 3.2 辅助功能

#### F5: 批量转换
- 支持文件夹批量转换
- 支持通配符匹配

#### F6: 版本管理
- 自动备份原文件
- 保留转换历史
- 支持回滚

#### F7: 格式检查
- 检查标题层级是否正确
- 检查引用格式
- 检查页眉页脚

### 3.3 扩展功能（后续）

#### F8: 在线文档集成（飞书/腾讯文档）

**适用场景**：公司内部文档在飞书、腾讯文档等在线协作平台

**支持平台**：
- 飞书文档（Feishu/Lark）
- 腾讯文档
- 语雀
- Notion
- Google Docs

**核心功能**：
- **拉取文档**：从在线平台下载文档到本地
- **推送文档**：将本地修改推送到在线平台
- **实时同步**：检测文档变更，自动同步
- **格式保留**：保留在线文档的格式和样式

**命令示例**：
```bash
# 飞书文档
dt pull feishu://docx/xxx123                    # 从飞书拉取文档
dt push ./doc.md feishu://docx/xxx123           # 推送到飞书

# 腾讯文档
dt pull tencent://sheet/xxx456                  # 从腾讯文档拉取
dt push ./doc.md tencent://sheet/xxx456         # 推送到腾讯文档

# 语雀
dt pull yuque://user/repo/xxx789                # 从语雀拉取
dt push ./doc.md yuque://user/repo/xxx789       # 推送到语雀
```

**技术方案**：
- 飞书：飞书开放平台 API + lark-oapi SDK
- 腾讯文档：腾讯文档 API
- 语雀：语雀 API
- 统一接口：抽象出通用的文档读写接口

---

## 4. 技术方案

### 4.1 技术栈

| 组件 | 技术选择 | 说明 |
|------|----------|------|
| 文档转换 | Pandoc | 业界标准，支持 40+ 种格式 |
| 格式修改 | python-docx | 直接操作 Word 文档内部结构 |
| 脚本封装 | Python | 跨平台，易于扩展 |
| CLI 工具 | Click/Argparse | 命令行界面 |
| 模板管理 | Jinja2 | 模板渲染（可选） |
| 飞书集成 | lark-oapi | 飞书开放平台官方 SDK |
| 腾讯文档集成 | 腾讯文档 API | 腾讯文档开放接口 |

### 4.2 架构设计

```
doc-transformer/
├── src/
│   ├── converter.py      # 核心转换逻辑（Pandoc）
│   ├── formatter.py      # 格式修改逻辑（python-docx）
│   ├── template.py       # 模板管理
│   ├── workflow.py       # 工作流管理
│   ├── integrations/     # 在线文档集成（扩展）
│   │   ├── feishu.py     # 飞书集成
│   │   ├── tencent.py    # 腾讯文档集成
│   │   ├── yuque.py      # 语雀集成
│   │   └── base.py       # 通用接口
│   └── cli.py            # 命令行入口
├── templates/
│   ├── thesis_cn.docx    # 中文论文模板
│   ├── thesis_en.docx    # 英文论文模板
│   ├── resume.docx       # 简历模板
│   └── report.docx       # 报告模板
├── tests/
│   ├── test_converter.py
│   ├── test_formatter.py
│   ├── test_workflow.py
│   └── test_integrations.py
├── docs/
│   └── PRD.md            # 本文档
├── requirements.txt
└── README.md
```

### 4.3 核心依赖

```txt
# MVP 阶段
pandoc>=3.0          # 文档转换
python-docx>=1.0     # Word 文档格式修改
click>=8.0           # CLI 框架

# 扩展阶段（在线文档集成）
lark-oapi>=1.3.0     # 飞书开放平台 SDK
```

### 4.4 核心流程

#### 工作流 A：转换编辑

**Word → Markdown**
```python
def docx_to_markdown(input_path, output_path=None):
    """
    1. 使用 Pandoc 将 .docx 转换为 .md
    2. 提取图片到 ./images/ 文件夹
    3. 清理格式噪音
    4. 保留原始文件备份
    """
    pass
```

**Markdown → Word**
```python
def markdown_to_docx(input_path, template=None, output_path=None):
    """
    1. 读取 Markdown 文件
    2. 应用模板样式（如果指定）
    3. 使用 Pandoc 转换为 .docx
    4. 验证格式完整性
    """
    pass
```

#### 工作流 B：直接修改格式

**格式修改**
```python
def format_docx(input_path, options, output_path=None):
    """
    使用 python-docx 直接修改 Word 文档格式

    参数：
    - font: 正文字体（如 "宋体"）
    - size: 正文字号（如 12）
    - heading_font: 标题字体
    - heading_size: 标题字号
    - line_spacing: 行距
    - margin_top: 上边距
    - margin_bottom: 下边距
    - margin_left: 左边距
    - margin_right: 右边距
    - template: 使用模板

    流程：
    1. 打开 .docx 文件
    2. 遍历所有段落
    3. 根据参数修改样式
    4. 保存为新文件（保留原文件备份）
    """
    pass
```

---

## 5. 用户界面

### 5.1 命令行界面（CLI）

```bash
# ==================== 工作流 A：转换编辑 ====================
# 转换为 Markdown
dt convert paper.docx                    # 转换为 Markdown
dt convert paper.docx --output my.md     # 指定输出文件名

# 转换回 Word
dt export paper.md                       # 转换回 Word
dt export paper.md --template thesis     # 使用模板转换

# 批量操作
dt convert ./docs/*.docx                 # 批量转换
dt export ./docs/*.md --template resume  # 批量导出

# ==================== 工作流 B：直接改格式 ====================
# 基本格式修改
dt format paper.docx --font "宋体" --size 12
dt format paper.docx --heading-font "黑体" --heading-size 16
dt format paper.docx --line-spacing 1.5
dt format paper.docx --margin-top 2.54cm --margin-bottom 2.54cm

# 使用模板修改格式
dt format paper.docx --template thesis_cn

# 组合修改
dt format paper.docx \
  --font "宋体" --size 12 \
  --heading-font "黑体" --heading-size 16 \
  --line-spacing 1.5 \
  --margin-top 2.54cm --margin-bottom 2.54cm

# ==================== 模板管理 ====================
dt template list                         # 列出可用模板
dt template add my_template.docx         # 添加自定义模板
dt template remove my_template           # 删除模板

# ==================== 其他 ====================
dt history                               # 查看转换历史
dt rollback paper.docx                   # 回滚到原始版本
```

### 5.2 与 Claude Code 集成

在 Claude Code 中可以直接使用：

```bash
# ==================== 工作流 A：转换编辑 ====================
# 转换文档
! dt convert paper.docx

# 编辑 Markdown
# Claude Code 直接读取和编辑 paper.md

# 导出
! dt export paper.md --template thesis

# ==================== 工作流 B：直接改格式 ====================
# 修改格式
! dt format paper.docx --font "宋体" --size 12

# 使用模板
! dt format paper.docx --template thesis_cn
```

---

## 6. 用户故事

### US1: 公众号作者（工作流 A）
```
作为一个公众号作者
我希望把 Word 初稿转换为 Markdown
然后在 Claude Code 中直接编辑内容
最后转换回 Word 发布
这样我不需要在多个工具间复制粘贴
```

### US2: 毕业生 - 内容编辑（工作流 A）
```
作为一个毕业生
我希望把论文转换为 Markdown
在 Claude Code 中编辑内容
然后使用论文模板导出
这样格式会自动符合学校要求
```

### US3: 毕业生 - 格式调整（工作流 B）
```
作为一个毕业生
我的论文内容已经确定
但格式不符合学校要求
我希望能直接修改格式
比如字体、字号、行距、页边距
这样我不需要手动调整每个段落
```

### US4: 内容创作者
```
作为一个内容创作者
我希望批量处理多个文档
统一转换格式
这样我可以高效处理大量内容
```

### US5: 飞书用户（工作流 C - 扩展功能）
```
作为一个飞书用户
我希望能在 Claude Code 中直接读取和编辑飞书文档
不需要复制粘贴
这样我可以高效处理公司内部文档
```

---

## 7. MVP 范围

### 第一阶段（MVP）
**工作流 A：转换编辑**
- [ ] Word → Markdown 转换
- [ ] Markdown → Word 转换
- [ ] 基本格式保留（标题、加粗、列表、表格）
- [ ] 图片提取和引用
- [ ] 自动备份

**工作流 B：直接改格式**
- [ ] 修改字体和字号
- [ ] 修改行距和段间距
- [ ] 修改页边距
- [ ] 使用模板修改格式

**CLI 工具**
- [ ] `dt convert` 命令
- [ ] `dt export` 命令
- [ ] `dt format` 命令

### 第二阶段
- [ ] 模板系统完善
- [ ] 批量转换
- [ ] 格式检查
- [ ] 转换历史
- [ ] 更多格式参数（页眉页脚、页码、目录）

### 第三阶段（扩展）
- [ ] 在线文档集成（工作流 C）
  - [ ] 飞书文档集成
  - [ ] 腾讯文档集成
  - [ ] 语雀集成
- [ ] Web 界面（可选）
- [ ] 更多格式支持（PDF、HTML）
- [ ] 与更多 AI Agent 集成
- [ ] 格式预览功能

---

## 8. 风险和限制

### 技术风险

**工作流 A（转换编辑）**
- **格式丢失**：复杂的 Word 格式可能无法完美保留
  - 缓解：使用模板系统，提供格式参考

- **图片处理**：嵌入式图片可能需要特殊处理
  - 缓解：提取到单独文件夹，Markdown 中使用相对路径

**工作流 B（直接改格式）**
- **复杂格式**：某些 Word 特有格式（如艺术字、SmartArt）可能无法处理
  - 缓解：专注于常见格式（字体、字号、行距、页边距）

- **模板兼容性**：不同版本的 Word 模板可能有差异
  - 缓解：测试主流 Word 版本，提供兼容性说明

**工作流 C（在线文档集成 - 扩展功能）**
- **API 权限**：飞书/腾讯文档需要申请应用权限
  - 缓解：提供详细的权限申请指南

- **格式兼容性**：在线文档格式与本地 Word 格式可能有差异
  - 缓解：使用平台原生 API，保留格式信息

- **实时协作冲突**：多人同时编辑可能产生冲突
  - 缓解：使用版本号检测，提示用户手动合并

### 用户风险
- **学习成本**：用户需要学习命令行
  - 缓解：提供简单的一键命令，文档清晰

---

## 9. 竞品分析

| 工具 | 优点 | 缺点 |
|------|------|------|
| **Pandoc** | 功能强大、格式多 | 命令复杂、学习曲线陡 |
| **python-docx** | 直接操作 Word 格式 | 只能处理 .docx，不支持其他格式 |
| **Typora** | 所见即所得 | 不支持 Word 导出、不是 CLI |
| **Mark Text** | 开源免费 | 功能有限 |
| **Zettlr** | 学术友好 | 界面复杂 |
| **飞书 MCP Server** | 支持飞书文档 | 只支持飞书，不支持本地文件 |

**我们的优势**：
1. 专为 AI Agent 设计
2. **三种工作流**：转换编辑 + 直接改格式 + 在线文档集成
3. Pandoc + python-docx 组合，覆盖内容和格式
4. 模板系统解决格式问题
5. 简单的 CLI 接口
6. 与 Claude Code 深度集成
7. 支持飞书、腾讯文档等在线协作平台

---

## 10. 下一步行动

### 立即行动
1. 安装 Pandoc 和 python-docx
2. 实现工作流 A（Word ↔ Markdown 转换）
3. 实现工作流 B（直接修改格式）
4. 创建第一个模板（毕业论文）

### 本周目标
- 完成核心转换功能
- 完成格式修改功能
- 测试几个真实文档
- 收集用户反馈

---

## 附录

### A. 技术参考
- Pandoc 官方文档：https://pandoc.org/
- python-docx 文档：https://python-docx.readthedocs.io/
- 飞书开放平台：https://open.feishu.cn/
- lark-oapi SDK：https://github.com/larksuite/oapi-sdk-python

### B. 格式支持列表

**工作流 A（转换编辑）**
- 输入格式：.docx, .pdf, .html, .txt
- 输出格式：.docx, .md, .pdf, .html

**工作流 B（直接改格式）**
- 支持格式：.docx
- 可修改项：
  - 段落：标题层级、对齐、行距、缩进
  - 字体：字体、字号、颜色、加粗/斜体
  - 页面：页边距、纸张大小、页眉页脚
  - 其他：页码、目录、项目符号

**工作流 C（在线文档集成 - 扩展功能）**
- 支持平台：飞书、腾讯文档、语雀
- 核心功能：拉取文档、推送文档、格式保留

### C. 模板示例

**毕业论文模板（thesis_cn.docx）**
```bash
# 应用模板
dt format paper.docx --template thesis_cn

# 模板包含的格式
- 正文：宋体，小四，1.5倍行距
- 标题：黑体，三号，居中
- 页边距：上下2.54cm，左右3.17cm
- 页眉页脚：学校名称和页码
```

### D. 在线文档集成示例

**飞书文档集成**
```bash
# 配置飞书应用
dt config feishu --app-id YOUR_APP_ID --app-secret YOUR_APP_SECRET

# 拉取飞书文档
dt pull feishu://docx/xxx123

# 编辑文档
# ... 在 Claude Code 中编辑 ...

# 推送回飞书
dt push ./doc.md feishu://docx/xxx123
```

**腾讯文档集成**
```bash
# 配置腾讯文档应用
dt config tencent --app-id YOUR_APP_ID --app-secret YOUR_APP_SECRET

# 拉取腾讯文档
dt pull tencent://sheet/xxx456

# 编辑文档
# ... 在 Claude Code 中编辑 ...

# 推送回腾讯文档
dt push ./doc.md tencent://sheet/xxx456
```
