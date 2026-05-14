from scene import create_scene
from config import scene_config
from elements import create_rectangle

rectangle_properties = {
    "name": "rectangle_one",
    "frame": 0,
    "size": [5, 5],
    "position": [2, 2],
    "fill": [255, 255, 255]
}

rectangle = create_rectangle(rectangle_properties)

rectangle.to([{
    "name": "position",
    "content": [2, 2]
}], 1)

elements = [rectangle]
create_scene(scene_config, elements)
