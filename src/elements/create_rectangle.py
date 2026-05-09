from utils import format_pixel

def create_rectangle(properties):
    color = properties["fill"]
    pixel = format_pixel(color)

    rectangle_appearance = (pixel * properties["size"][0] + "\n") * properties["size"][1]

    rectangle = {
        "rectangle_appearance": rectangle_appearance,
        "position": properties["position"]
    }

    return rectangle
