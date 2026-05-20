# DocTransformer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 让 AI Agent 能够直接识别、编辑 Word/PDF 文档的工具链

[English](#english) | [中文](#中文)

---

## 中文

### 简介

DocTransformer 是一个专为 AI Agent（如 Claude Code、Cursor）设计的文档转换工具。它解决了"上传-复制-粘贴"的低效流程，让你可以直接在 AI Agent 中编辑 Word 文档。

### 核心功能

| 工作流 | 功能 | 适用场景 |
|--------|------|----------|
| **A：转换编辑** | Word ↔ Markdown 双向转换 | 内容需要大改 |
| **B：直接改格式** | 直接修改 Word 文档格式 | 内容已定，只调格式 |

### 安装

```bash
# 1. 安装 Pandoc（文档转换引擎）
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt install pandoc

# Windows
# 从 https://pandoc.org/installing.html 下载安装

# 2. 安装 DocTransformer
pip install doc-transformer
```

### 快速开始

#### 工作流 A：转换编辑（适合内容修改）

```bash
# 1. 将 Word 转换为 Markdown
dt convert paper.docx

# 2. 在 Claude Code 或任何编辑器中编辑 paper.md
# ... 修改内容 ...

# 3. 将 Markdown 转换回 Word
dt export paper.md
```

#### 工作流 B：直接改格式（适合格式调整）

```bash
# 修改字体和字号
dt format paper.docx --font "宋体" --size 12

# 使用内置模板
dt format paper.docx --template thesis_cn

# 自定义格式
dt format paper.docx \
  --font "楷体" --size 14 \
  --heading-font "黑体" --heading-size 18 \
  --heading-color blue \
  --line-spacing 1.5 \
  --margin-top 2.54cm --margin-bottom 2.54cm
```

### 命令列表

| 命令 | 说明 |
|------|------|
| `dt convert <file>` | Word → Markdown |
| `dt export <file>` | Markdown → Word |
| `dt format <file>` | 修改 Word 格式 |
| `dt templates` | 查看可用模板 |
| `dt batch <pattern>` | 批量转换 |

### 可用模板

| 模板 | 说明 | 格式 |
|------|------|------|
| `thesis_cn` | 中文论文 | 宋体小四，1.5倍行距 |
| `thesis_en` | 英文论文 | Times New Roman 12pt，2.0倍行距 |
| `resume` | 简历 | 微软雅黑小四，1.25倍行距 |

### 格式参数

| 参数 | 说明 | 示例值 |
|------|------|--------|
| `--font` | 正文字体 | `宋体`、`Times New Roman` |
| `--size` | 正文字号 | `12`、`小四`、`四号` |
| `--color` | 正文颜色 | `red`、`blue`、`#FF0000` |
| `--heading-font` | 标题字体 | `黑体` |
| `--heading-size` | 标题字号 | `16`、`三号` |
| `--heading-color` | 标题颜色 | `blue` |
| `--line-spacing` | 行距 | `1.5`、`2.0` |
| `--margin-top` | 上边距 | `2.54cm` |
| `--margin-bottom` | 下边距 | `2.54cm` |
| `--margin-left` | 左边距 | `3.17cm` |
| `--margin-right` | 右边距 | `3.17cm` |
| `--alignment` | 对齐方式 | `left`、`center`、`justify` |
| `--first-line-indent` | 首行缩进 | `2cm` |

### 使用场景

#### 场景 1：公众号推文优化

```bash
# 转换
dt convert 推文初稿.docx

# 在 Claude Code 中编辑内容
# "帮我优化这篇文章的标题和开头..."

# 导出
dt export 推文初稿.md
```

#### 场景 2：毕业论文格式调整

```bash
# 一键应用论文格式
dt format 论文.docx --template thesis_cn
```

#### 场景 3：自定义格式

```bash
dt format 报告.docx \
  --font "微软雅黑" --size 12 \
  --heading-font "黑体" --heading-size 16 --heading-color blue \
  --line-spacing 1.5 \
  --margin-top 2cm --margin-bottom 2cm
```

### 与 AI Agent 集成

DocTransformer 可以与 Claude Code、Cursor 等 AI Agent 无缝集成：

```bash
# 在 Claude Code 中
! dt convert paper.docx
# 直接编辑 paper.md
! dt export paper.md
```

### 开发

```bash
# 克隆项目
git clone https://github.com/YOUR_USERNAME/doc-transformer.git
cd doc-transformer

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest tests/
```

### 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

### 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## English

### Introduction

DocTransformer is a document conversion toolchain designed for AI Agents (like Claude Code, Cursor). It solves the inefficient "upload-copy-paste" workflow by allowing you to edit Word documents directly in AI Agents.

### Features

| Workflow | Function | Use Case |
|----------|----------|----------|
| **A: Convert & Edit** | Word ↔ Markdown conversion | Major content changes |
| **B: Format Only** | Direct format modification | Format adjustments only |

### Installation

```bash
# 1. Install Pandoc
brew install pandoc  # macOS
sudo apt install pandoc  # Linux

# 2. Install DocTransformer
git clone https://github.com/VVVickyA/doc-transformer.git
cd doc-transformer
pip install -e .
```

### Quick Start

```bash
# Convert Word to Markdown
dt convert paper.docx

# Edit paper.md in Claude Code or any editor

# Convert back to Word
dt export paper.md

# Or modify format directly
dt format paper.docx --template thesis_cn
```

### License

MIT

---

## 参与贡献

1. Fork 本项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 作者

- **VVVickyA** - [GitHub](https://github.com/VVVickyA)

## 致谢

- [Pandoc](https://pandoc.org/) - 文档转换引擎
- [python-docx](https://python-docx.readthedocs.io/) - Word 文档处理库
- [Click](https://click.palletsprojects.com/) - CLI 框架
