from elements import create_background
from scene import add_body, generate_frame

def create_scene(config, elements):
    headers = (
        "P3"
        "\n"
        f"{config["resolution"][0]} {config["resolution"][1]}"
        "\n"
        "255"
    )

    background = create_background(config["background_color"], config["resolution"])
    body = add_body(elements, background)

    frame = (
        f"{headers}\n"
        f"{body}"
    )

    generate_frame(frame)
