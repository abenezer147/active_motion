from scene import create_scene
from config import scene_config
from elements import create_rectangle

rectangle_properties = {
    "size": [20, 20],
    "position": [7, 0],
    "fill": [255, 255, 255]
}

rectangle = create_rectangle(rectangle_properties)
elements = [rectangle]

create_scene(scene_config, elements)
