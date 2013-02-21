from pygame.color import Color

class Field():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.fields = []
        for i in range(height):
            self.fields.append([Color(20,20,20,255) for j in range(width)])


    def __str__(self):
        repr = ""
        for i in range(self.height):
            repr += str(self.fields[i])
            repr += "\n"
        return repr


