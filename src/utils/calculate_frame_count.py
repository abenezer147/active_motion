from config import scene_config

def calculate_frame_count(time):
    frame_count = time * scene_config["fps"]
    return frame_count
