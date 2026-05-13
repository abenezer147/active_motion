class Rectangle:
    def __init__(self, properties, content):
        self.properties = properties
        self.content = content

    def to(self, new_properties):
        for new_property in new_properties:
            self.properties[new_property["name"]] = new_property["content"]
