from elements import create_element
from utils import format_pixel

def create_rectangle(properties):
    color = properties["fill"]
    pixel = format_pixel(color)

    rectangle = {
        "properties": properties,
        "content": create_element(pixel, properties["size"])
    }

    return rectangle
