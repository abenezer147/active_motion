class Rectangle:
    def __init__(self, properties, content):
        self.content = content
        self.frames = []

        self.frames.append({
            "properties": properties,
            "content": self.content
        })

    def to(self, new_properties,):
        for new_property in new_properties:
            self.frames.append({
                "properties": new_property,
                "content": self.content
            })

