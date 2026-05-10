from utils import create_rows

def create_element(pixel, size):
    width = size[0]

    element = []

    for _ in range(size[1]):
        row = create_rows(pixel, width)
        element.append(row)

    return element
