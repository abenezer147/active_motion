def format_pixel(pixel_color):
    pixel = ""

    for value in pixel_color:
        str_value = str(value)
        pixel += str_value + (" " * (3 - len(str_value)))

    return pixel
