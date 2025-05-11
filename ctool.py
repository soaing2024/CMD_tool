def hex_to_rgb(hex_color):
    """将十六进制颜色代码转换为RGB元组"""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) != 6:
        raise ValueError("Invalid hex color code")
    return (
        int(hex_color[0:2], 16),
        int(hex_color[2:4], 16),
        int(hex_color[4:6], 16)
    )


def rprint(text, color=None, bg_color=None, end='', **styles):
    """
    在命令行输出彩色文本

    :param text: 要输出的文本
    :param color: 十六进制前景色（如#123456）
    :param bg_color: 十六进制背景色（如#abcdef）
    :param end: 结束符（默认不换行）
    :param styles: 文本样式（支持bold, underline, italic）
    """
    ansi_codes = []

    # 处理文本样式
    style_map = {
        'bold': 1,
        'underline': 4,
        'italic': 3
    }
    for style, code in style_map.items():
        if styles.get(style):
            ansi_codes.append(str(code))

    # 处理前景色
    if color:
        r, g, b = hex_to_rgb(color)
        ansi_codes.extend(['38', '2', str(r), str(g), str(b)])

    # 处理背景色
    if bg_color:
        r, g, b = hex_to_rgb(bg_color)
        ansi_codes.extend(['48', '2', str(r), str(g), str(b)])

    # 构建ANSI转义序列
    if ansi_codes:
        ansi_seq = f'\033[{";".join(ansi_codes)}m'
        reset_seq = '\033[0m'
        text = f'{ansi_seq}{text}{reset_seq}'

    print(text, end=end)

