# LearnAI Vue3 前端

🚀 基于 Vue3 的现代化 AI 聊天界面

## ✨ 特性

### 🎨 现代化设计
- **渐变背景** - 美观的紫色渐变背景
- **毛玻璃效果** - 现代化的半透明设计
- **流畅动画** - 消息滑入、按钮悬停等动画效果
- **响应式布局** - 完美适配桌面和移动设备

### 🤖 智能交互
- **实时状态显示** - 在线/离线状态指示器
- **输入指示器** - AI思考时的动态加载效果
- **快捷操作** - 预设的常用问题快速开始对话
- **字符计数** - 实时显示输入字符数和限制

### 🛠️ 实用功能
- **对话导出** - 支持导出聊天记录为文本文件
- **清空对话** - 一键清除所有聊天记录
- **错误处理** - 友好的错误提示和自动重试
- **连接监控** - 自动检测API连接状态

### ⌨️ 便捷操作
- **快捷键支持** - Enter发送，Shift+Enter换行
- **自动调整** - 输入框高度自动调整
- **自动滚动** - 新消息自动滚动到底部
- **焦点管理** - 页面加载后自动聚焦输入框

## 📁 文件结构

```
frontend/
├── index.html          # 原版前端（备用）
├── index-vue3.html     # Vue3 现代化前端（主要）
├── vue-app.html        # Vue3 单页应用版本
├── package.json        # 项目依赖配置
├── vite.config.js      # Vite 构建配置
└── README.md          # 说明文档
```

## 🚀 快速开始

### 方式一：直接使用（推荐）

1. 启动后端服务：
```bash
cd /Users/cuiziliang/Projects/LearnAI/LearnAI
python -m uvicorn src.agent.webapp:app --reload --host 0.0.0.0 --port 8000
```

2. 打开浏览器访问：
```
http://localhost:8000
```

现在会自动加载 Vue3 版本的前端界面！

### 方式二：开发环境（可选）

如果需要进行前端开发，可以安装依赖：

```bash
cd frontend
npm install
npm run dev
```

## 🎯 使用指南

### 开始对话
1. **快捷操作** - 点击欢迎页面的预设问题快速开始
2. **直接输入** - 在底部输入框输入您的问题
3. **快捷键** - 使用 Enter 发送，Shift+Enter 换行

### 管理对话
- **清空对话** - 点击输入框右侧的垃圾桶图标
- **导出记录** - 点击下载图标导出聊天记录
- **查看状态** - 右上角显示连接状态

### 错误处理
- 网络错误会自动显示错误提示
- 错误信息会在5秒后自动消失
- 可以手动点击关闭错误提示

## 🔧 技术栈

- **Vue 3** - 渐进式 JavaScript 框架
- **Composition API** - Vue3 的组合式 API
- **Axios** - HTTP 客户端库
- **Font Awesome** - 图标库
- **CSS3** - 现代化样式和动画

## 🎨 设计特色

### 颜色方案
- **主色调** - 紫色渐变 (#667eea → #764ba2)
- **成功色** - 绿色渐变 (#10b981 → #059669)
- **背景色** - 浅灰色系 (#f8fafc)
- **文本色** - 深灰色系 (#374151)

### 动画效果
- **消息滑入** - 新消息从下方滑入
- **按钮悬停** - 鼠标悬停时的缩放和阴影效果
- **输入指示器** - 三个点的跳动动画
- **状态指示器** - 脉冲动画显示在线状态

### 响应式设计
- **桌面端** - 最大宽度1000px，居中显示
- **平板端** - 自适应宽度，优化触摸操作
- **手机端** - 全屏显示，简化界面元素

## 🔄 版本对比

| 特性 | 原版 (index.html) | Vue3版 (index-vue3.html) |
|------|------------------|-------------------------|
| 框架 | 原生 JavaScript | Vue 3 |
| 设计 | 基础样式 | 现代化设计 |
| 动画 | 简单过渡 | 丰富动画效果 |
| 功能 | 基础聊天 | 增强功能 |
| 响应式 | 基本支持 | 完全响应式 |
| 错误处理 | 简单提示 | 完善的错误处理 |
| 用户体验 | 良好 | 优秀 |

## 🛠️ 自定义配置

### 修改主题色
在 CSS 的 `:root` 选择器中修改 CSS 变量：

```css
:root {
    --primary-gradient: linear-gradient(135deg, #your-color1, #your-color2);
    --success-gradient: linear-gradient(135deg, #your-color3, #your-color4);
}
```

### 调整动画速度
修改 CSS 中的 `transition` 和 `animation` 属性的时间值。

### 更改API端点
在 JavaScript 中修改 API 调用的 URL。

## 📱 浏览器兼容性

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+
- ⚠️ IE 不支持

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

MIT License