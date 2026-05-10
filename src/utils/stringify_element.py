def stringify_element(element):
    stringified_rows = []

    for row in element:
        stringified_row = "".join(row)
        stringified_rows.append(stringified_row)

    stringified_element = "\n".join(stringified_rows)
    return stringified_element
