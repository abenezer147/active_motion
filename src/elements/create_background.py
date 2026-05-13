from elements import create_element, Background
from utils import format_pixel

def create_background(background_color, size):
    pixel = format_pixel(background_color)
    content = create_element(pixel, size)

    background = Background(content)
    return background

