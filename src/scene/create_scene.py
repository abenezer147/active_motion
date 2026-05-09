def create_scene(config):
    headers = (
        "P3"
        f"\n{config["resolution"][0]} {config["resolution"][1]}"
    )

    print(headers)
