from app.models.colour import Colour

class Tag:

    def __init__(self, name, colour, active = True, reserved = False, id = None):

        self.name = name
        self.colour = colour
        self.active = active
        self.reserved = reserved
        self.id = id

    def deactivate(self):

        if not self.reserved:
            self.active = False

    def activate(self):

        if not self.reserved:
            self.active = True

    def change_colour(self, colour):
        self.colour = colour