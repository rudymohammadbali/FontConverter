from font_converter import convert_font


def success_callback(msg: str):
    print(msg)


def failure_callback(msg: str):
    print(msg)


convert_font('Roboto-Regular.ttf', './', 'otf', success_callback, failure_callback)

