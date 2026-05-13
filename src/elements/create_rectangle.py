from elements import create_element, Rectangle
from utils import format_pixel

def create_rectangle(properties):
    color = properties["fill"]
    pixel = format_pixel(color)

    content = create_element(pixel, properties["size"])
    rectangle = Rectangle(properties, content)

    return rectangle
