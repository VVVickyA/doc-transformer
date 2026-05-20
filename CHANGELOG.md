# 更新日志

本项目的所有重要更改都会记录在此文件。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [0.1.0] - 2026-05-20

### 新增
- 工作流 A：Word ↔ Markdown 双向转换
- 工作流 B：直接修改 Word 文档格式
- 内置模板系统（中文论文、英文论文、简历）
- 支持自定义格式（字体、字号、颜色、行距、页边距等）
- 批量转换功能
- 自动备份原文件
- CLI 工具 `dt`

### 依赖
- Pandoc >= 3.0
- python-docx >= 1.0
- click >= 8.0
