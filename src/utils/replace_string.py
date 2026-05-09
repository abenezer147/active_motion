def replace_string(original_string, replacement_string, start_position):
    pixel_start_position = 9 * start_position
    replacement_length = len(replacement_string) + 1

    new_string = original_string[:start_position] + replacement_string + original_string[replacement_length:]
    return new_string
