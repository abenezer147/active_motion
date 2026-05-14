from utils import stringify_element, group_elements

def add_body(elements, background):
    frames = group_elements(elements)

    for element in elements:
        element_x = element.frames[0]["properties"]["position"][0]
        element_y = element.frames[0]["properties"]["position"][1]
        element_content = element.frames[0]["content"]

        for i, row in enumerate(element_content):
            actual_y_position = i + element_y

            if actual_y_position < 0 or actual_y_position >= len(background.content):
                continue

            for j, pixel in enumerate(row):
                actual_x_position = j + element_x

                if actual_x_position < 0 or actual_x_position >= len(background.content[i + element_y]):
                    continue

                background.content[i + element_y][j + element_x] = pixel

    stringified_background = stringify_element(background.content)
    body = stringified_background

    return body
