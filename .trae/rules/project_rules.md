# 项目规则

## 1. 命名规范

所有变量名称、CSS 类名、ID 名称必须以 `tx_` 开头。

**示例：**

```html
<div id="tx_header" class="tx_container tx_card"></div>
```

```css
.tx_container {
    padding: 16px;
}
#tx_header {
    background: #fff;
}
```

```javascript
let tx_userName = '唐笑';
const tx_apiUrl = '/api/data';
function tx_fetchData() { ... }
```

## 2. HTML 页面头部注释

所有 HTML 页面 `<html>` 标签之后、`<head>` 之前必须包含如下格式的注释块，占位符在生成页面时替换为实际内容：

```html
<!--
姓名：唐笑
日期：YYYY-MM-DD
功能名称：<页面功能简要描述>
-->
```

**示例：**

```html
<!DOCTYPE html>
<html lang="zh-CN">
<!--
姓名：唐笑
日期：2026-10-22
功能名称：养宠帮首页
-->
<head>
    ...
</head>
```

## 3. 技术栈

- **HTML / CSS / JavaScript**：全部使用原生实现，不使用任何前端框架或第三方库
- **图标**：统一使用 `font/` 目录下的 iconfont 图标，不引用外部图标库
- **数据请求**：使用原生 `fetch` API 获取服务器端数据，不使用 axios、jQuery 等
- **不使用任何 CDN**，所有资源（字体、样式、脚本）均来自项目本地
