from scene import create_scene
from config import scene_config
from elements import create_rectangle

rectangle_properties = {
    "size": [5, 5],
    "position": [9, 0],
    "fill": [255, 100, 0]
}

rectangle = create_rectangle(rectangle_properties)

elements = [rectangle]

create_scene(scene_config, elements)
