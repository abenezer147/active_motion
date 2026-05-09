from utils import format_pixel

def create_background(background_color, size):
    pixel = format_pixel(background_color)

    background = (pixel * size[0] + "\n") * size[1]
    return background

