from utils import replace_string

def add_body(elements, background):
    background_rows = background.split("\n")

    for element in elements:
        appearance = element["appearance"]
        appearance_rows = appearance.split("\n")

        position = element["position"]

        i = 0
        for row in appearance_rows:
            new_string = replace_string(background_rows[position[1] + i], row, position[0])
            background_rows[position[1] + i] = new_string

            i += 1

    body = "\n".join(background_rows)
    return body
