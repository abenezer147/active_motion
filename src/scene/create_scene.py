from scene import create_background, add_body

def create_scene(config, elements):
    headers = (
        "P3"
        "\n"
        f"{config["resolution"][0]} {config["resolution"][1]}"
    )

    background = create_background(config["background_color"], config["resolution"])
    body = add_body(elements, background)

    frame = (
        f"{headers}\n"
        f"{body}"
    )

    print(frame)
