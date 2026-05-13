from scene import create_scene
from config import scene_config
from elements import create_rectangle

rectangle_properties = {
    "name": "rectangle_one",
    "size": [5, 5],
    "position": [0, 0],
    "fill": [255, 255, 255]
}

rectangle = create_rectangle(rectangle_properties)

elements = [rectangle]

create_scene(scene_config, elements)
