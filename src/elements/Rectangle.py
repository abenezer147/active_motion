from utils import calculate_frame_count

class Rectangle:
    def __init__(self, properties, content):
        self.content = content
        self.frames = []

        self.frames.append({
            "properties": properties,
            "content": self.content
        })

    def to(self, new_properties, end_time):
        applied_properties = self.frames[0]["properties"]
        applied_properties["frame"] = calculate_frame_count(end_time)

        for new_property in new_properties:
            applied_properties[new_property["name"]] = new_property["content"]

        self.frames.append({
            "properties": applied_properties,
            "content": self.content
        })

