# DeepSeek2Chatbox | 让思考过程可见的R1 | [EN](https://github.com/chadyi/DeepSeek2Chatbox/blob/main/README_EN.md)

一个轻量级的API转发服务，让你在Chatbox中看到DeepSeek模型的完整思考过程。

## 这是什么？
硅基流动最近将API接口升级为DeepSeek官方格式，响应被分为两部分：
- reasoning_content：模型的思考过程
- content：最终的回答

这导致Chatbox无法显示模型的思考过程。本项目通过API转发，将两部分内容优雅地合并，让你能完整体验模型的思考全过程。

## 开始使用

### 方式一：直接使用
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
4. 部署到服务器并添加SSL
5. 在Chatbox中使用：`http://你的域名:5000/v1`

## 效果展示
你将看到这样的输出：

![image](https://github.com/user-attachments/assets/b2003a8a-8839-4b30-b95f-31ca22a89a89)

## 特点
- 🔄 实时转发：无延迟，所见即所得
- 🧠 思维可见：让AI的思考过程不再是黑盒
- 🎯 即插即用：完全兼容Chatbox
- 🪶 轻量简单：无需复杂配置

## 问题反馈
遇到问题？欢迎提交Issue或联系作者。
