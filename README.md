# CMD_tool
最简单的命令行组件工具。持续更新。

## ✨ 特性
- 🎨 支持十六进制颜色代码（前景色/背景色）
- 💪 纯Python实现，零依赖
- 📝 支持多种文本样式（加粗/斜体/下划线）
- ⚡ 自动样式重置，无需手动恢复终端设置
- 🔧 兼容大多数现代终端（支持ANSI转义码）

## 📥 安装
直接复制 `ctool.py` 到您的项目目录，或：

## 🚀 使用方法
### 基本函数

rprint(
    text: str,           # 要打印的文本
    color: str = None,   # 前景色（十六进制 如#ff0000）
    bg_color: str = None,# 背景色（十六进制 如#00ff00）
    end: str = '',       # 结束符（默认不换行）
    **styles: bool       # 样式参数（bold/underline/italic）
)

### 示例代码

from ctool import rprint

rprint('红色警告', color='#ff0000', bold=True)  # 基础颜色
rprint('绿色背景', bg_color='#00ff00')

rprint('蓝字黄底+斜体', 
       color='#0000ff', 
       bg_color='#ffff00', 
       italic=True)  # 组合样式

for i in range(0, 256, 5):
    rprint('■', color=f'#{i:02x}00ff')  # 渐变效果

for percent in range(0, 101):
    color = f'#{percent*2:02x}{100-percent:02x}00'
    rprint(f'\r进度: {percent}% ', color=color, end='')
    time.sleep(0.1)  # 进度条模拟

headers = ['ID', 'Status', 'Message']
data = [
    ('#ff5555', 'ERROR', 'File not found'),
    ('#55ff55', 'OK', 'Operation succeeded')
]

for color, status, msg in data:
    rprint(f'{status:^8}', color=color, end='|')
    rprint(f'{msg:^20}', bg_color='#444444', end='\n')  # 表格输出

## ⚠️ 注意事项
需要终端支持真彩色：

✅ 推荐：VSCode、Windows Terminal、iTerm2

⚠️ 部分支持：macOS默认终端（需手动启用真彩色）

### 颜色格式要求：

必须为6位十六进制（支持#123abc，不支持#123简写）

颜色代码需包含#前缀

### 样式兼容性：

斜体在部分终端可能显示为反白颜色

下划线样式可能与某些字体不兼容