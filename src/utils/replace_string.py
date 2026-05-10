def replace_string(original_string, replacement_string, start_position):
    pixel_start_position = start_position * 6
    replacement_length = (len(replacement_string.split(" ")) - 1) * 2

    new_string = original_string[:pixel_start_position] + replacement_string + original_string[replacement_length:]

    return new_string
