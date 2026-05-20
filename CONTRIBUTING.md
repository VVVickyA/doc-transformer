# 贡献指南

感谢你对 DocTransformer 项目的关注！我们欢迎任何形式的贡献。

## 如何贡献

### 报告 Bug

1. 在 [Issues](https://github.com/YOUR_USERNAME/doc-transformer/issues) 页面创建新 Issue
2. 描述清楚问题和复现步骤
3. 如果可能，提供错误日志和截图

### 提交功能建议

1. 在 Issues 页面创建新 Issue，标题以 `[Feature]` 开头
2. 详细描述你希望添加的功能和使用场景

### 提交代码

1. Fork 本项目
2. 创建功能分支：`git checkout -b feature/你的功能名`
3. 提交更改：`git commit -m '添加了某某功能'`
4. 推送到分支：`git push origin feature/你的功能名`
5. 创建 Pull Request

### 开发环境设置

```bash
# 克隆项目
git clone https://github.com/YOUR_USERNAME/doc-transformer.git
cd doc-transformer

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate  # Windows

# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest tests/
```

### 代码规范

- 遵循 PEP 8 代码规范
- 添加必要的注释和文档字符串
- 确保所有测试通过

### 提交规范

提交信息格式：
```
<类型>: <描述>

[可选] 详细说明
```

类型包括：
- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式调整
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建/工具相关

### Pull Request 规范

- PR 标题简洁明了
- 描述清楚做了什么改动、为什么这么做
- 关联相关的 Issue
- 确保 CI 通过

## 问题反馈

如有任何问题，欢迎在 Issues 页面反馈。

## 许可证

贡献的代码将采用 MIT 许可证。
