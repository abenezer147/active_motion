from elements import create_element
from utils import format_pixel

def create_background(background_color, size):
    pixel = format_pixel(background_color)
    background = create_element(pixel, size)

    return background

