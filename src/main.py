from scene import create_scene
from config import scene_config
from elements import create_rectangle

rectangle_properties = {
    "size": [500, 500],
    "position": [0, 0],
    "fill": [255, 255, 255]
}

rectangle = create_rectangle(rectangle_properties)

elements = [rectangle]

create_scene(scene_config, elements)
