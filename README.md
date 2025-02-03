# DeepSeek2Chatbox | 让思考过程可见的R1 | [EN](README_EN.md)

一个轻量级的API转发服务，让你在Chatbox中看到DeepSeek模型的完整思考过程。并删去历史对话中的推理过程，节约token。

## 这是什么？
硅基流动最近将API接口升级为DeepSeek官方格式，响应被分为两部分：
- reasoning_content：模型的思考过程
- content：最终的回答

这导致部分版本Chatbox无法显示模型的思考过程。本项目通过API转发，将两部分内容优雅地合并，让你能完整体验模型的思考全过程。

## 开始使用

### 方式一：直接使用
1. 打开Chatbox，添加新对话模型
2. 填写配置：
   - 名称：任意（如：DeepSeek-R1）
   - 模型：deepseek-ai/DeepSeek-R1
   - API地址：
     - 基础版：`https://deepseek2chatbox.dawne.cn/v1`
     - 搜索版：`https://deepseek2chatbox.dawne.cn/v1/chat/completions/with-search`
   - API Key：你的硅基流动API Key（以sk-开头）

### 方式二：自行部署
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
