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

## 效果展示

![image](https://github.com/user-attachments/assets/43447fc6-0c70-4db9-84ca-7e393603abed)

## 问题反馈
遇到问题？欢迎提交Issue或联系作者。
