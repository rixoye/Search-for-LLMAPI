# Search-for-LLMAPI | 大模型 API 联网搜索增强 | [EN](README_EN.md)

## 这是什么？
一个轻量级的 API 增强服务，为各大模型 API 添加实时联网搜索能力，让 AI 回答更加准确、及时。

## 🌟 主要特点

- 🔍 **实时联网搜索**：自动检测需要搜索的问题，实时获取最新信息
- 🎯 **多平台支持**：支持多个主流大模型平台的 API，包括：
  - SiliconFlow (硅基流动)
  - 百度文心千帆
  - 字节跳动火山引擎
  - 阿里云通义千问
  - InfiniAI
  - 腾讯知识引擎
- 🤔 **思维链展示**：支持展示 DeepSeek 模型的完整思考过程
- 🧹 **自动清理**：自动清理历史记录中的思考过程，保持对话整洁

## 开始使用

### 方式一：直接使用
1. 在客户端中（如 Chatbox）添加新对话模型
2. 填写配置：
   - API地址：`https://search-for-llmapi.dawne.cn/with-search/v1/chat/completions`
   - 不带搜索版 API地址：`https://search-for-llmapi.dawne.cn/v1/chat/completions`
   - API Key：你的模型平台 API Key（如硅基流动的 sk-xxx）
   - 模型：`平台@模型名`（如：`siliconflow@deepseek-ai/deepseek-coder-33b-instruct`）
   - 具体请看 https://eqrwxrl391e.feishu.cn/wiki/TEwxweXOOi5I2lk60VocY9QOnob


### 方式二：自行部署(完善中)
1. 克隆仓库
2. 安装依赖：
   ```bash
   pip install flask requests
   ```
3. 启动服务：
   ```bash
   python server.py
   ```
4. 部署到服务器并添加SSL
5. 在Chatbox中使用：`https://你的域名/v1`或`https://你的域名/v1/chat/completions/with-search`

## 功能特点

### 基础功能
- 🔄 实时转发：无延迟，所见即所得
- 🧠 思维可见：让AI的思考过程不再是黑盒
- 🎯 即插即用：完全兼容Chatbox
- 🪶 轻量简单：无需复杂配置
- 🧹 自动清理：历史记录中的思考过程会被自动清理，保持对话整洁

### 搜索增强（新）
- 🔍 智能搜索：使用GLM-4优化搜索关键词
- 📚 实时资讯：自动获取相关网络信息
- 🎯 精准回答：基于搜索结果提供更准确的回答

## 效果展示

### 基础对话
![基础对话效果](https://github.com/user-attachments/assets/b2003a8a-8839-4b30-b95f-31ca22a89a89)

### 搜索增强对话
```
用户：openai最近有什么新功能？

[搜索结果]
- [OpenAI推出ChatGPT新功能Tasks 助力用户高效管理生活](https://news.pconline.com.cn/1869/18699469.html)
- [报道称OpenAI即将推出ChatGPT新功能：自动搞定餐厅预订和旅行规划](https://finance.sina.com.cn/world/2025-01-23/doc-inefxarn5053654.shtml)
...

<think>
[模型思考过程]
</think>

[模型基于搜索结果的回答]
```

## 问题反馈
遇到问题？欢迎提交Issue或联系作者。
