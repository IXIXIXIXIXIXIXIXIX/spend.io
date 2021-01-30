class Merchant:

    def __init__(self, name, default_tag, active = True, id = None):
        self.name = name.upper()
        self.default_tag = default_tag
        self.id = id
        self.active = active


    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def change_default(self, new_tag):

        if new_tag.active:
            self.default_tag = new_tag