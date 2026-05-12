from scene import create_scene
from config import scene_config
from elements import create_rectangle

rectangle_one_properties = {
    "size": [3, 3],
    "position": [0, 0],
    "fill": [255, 255, 255]
}

rectangle_two_properties = {
    "size": [3, 3],
    "position": [3, 3],
    "fill": [0, 0, 0]
}

rectangle_three_properties = {
    "size": [3, 3],
    "position": [6, 6],
    "fill": [255, 255, 255]
}

rectangle_four_properties = {
    "size": [3, 3],
    "position": [9, 9],
    "fill": [0, 0, 0]
}

rectangle_one = create_rectangle(rectangle_one_properties)
rectangle_two = create_rectangle(rectangle_two_properties)
rectangle_three = create_rectangle(rectangle_three_properties)
rectangle_four = create_rectangle(rectangle_four_properties)

elements = [
    rectangle_one,
    rectangle_two,
    rectangle_three,
    rectangle_four
]

create_scene(scene_config, elements)
