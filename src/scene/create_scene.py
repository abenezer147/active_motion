def create_scene(config, elements):
    headers = (
        "P3"
        "\n"
        f"{config["resolution"][0]} {config["resolution"][1]}"
    )
