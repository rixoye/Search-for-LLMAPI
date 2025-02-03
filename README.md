# DeepSeek2Chatbox | 让思考过程可见的硅基R1 | [EN](https://github.com/chadyi/DeepSeek2Chatbox/blob/main/README_EN.md)

一个轻量级的API转发服务，让你在Chatbox中看到DeepSeek模型的完整思考过程。

## 这是什么？
硅基流动最近将API接口升级为DeepSeek官方格式，响应被分为两部分：
- reasoning_content：模型的思考过程
- content：最终的回答

这导致Chatbox无法显示模型的思考过程。本项目通过API转发，将两部分内容优雅地合并，让你能完整体验模型的思考全过程。

## 开始使用

### 方式一：直接使用（推荐）
1. 打开Chatbox，添加新对话模型
2. 填写配置：
   - 名称：任意（如：DeepSeek-R1）
   - 模型：deepseek-ai/DeepSeek-R1
   - API地址：`https://deepseek2chatbox.dawne.cn/v1`
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
4. 在Chatbox中使用：`http://localhost:9006/v1`

## 效果展示
你将看到这样的输出：

<think>用户发来了简单的问候。让我思考如何回应：首先要表达友好，同时展现专业性。可以加入适当的表情符号增加亲和力。回答要简洁但不失温度，同时为后续对话留下开放性。
</think>

你好！很高兴见到你👋 有什么我可以帮你的吗？

## 特点
- 🔄 实时转发：无延迟，所见即所得
- 🧠 思维可见：让AI的思考过程不再是黑盒
- 🎯 即插即用：完全兼容Chatbox
- 🪶 轻量简单：无需复杂配置

## 问题反馈
遇到问题？欢迎提交Issue或联系作者。
