def printmsg(msg, style):
    def style_asterisk():
        nonlocal style
        style *= 20

    def style_equals():
        nonlocal style
        style *= 10

    if style == '*':
        style_asterisk()
    elif style == '=':
        style_equals()

    print(style, "\n", msg, "\n", style)


printmsg("HELLO", '*')
printmsg("HELLO", '=')
