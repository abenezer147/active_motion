import re

def list_pixels(row):
    row_pixels = re.findall(r"((?:[^\s]*?\s){2}[^\s]*?)\s", row)

    return row_pixels
