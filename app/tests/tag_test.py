import unittest
from app.models.tag import Tag
from app.models.colour import Colour 

class TestTag(unittest.TestCase):

    def setUp(self):
        self.colour1 = Colour("black")
        self.colour2 = Colour("red")

        self.tag = Tag("misc", self.colour1)
        self.reserved_tag = Tag("misc_2", self.colour1, True, True)


    def test_tag_has_name(self):
        self.assertEqual("misc", self.tag.name)

    def test_tag_has_colour(self):
        self.assertEqual(self.colour1, self.tag.colour)

    def test_tag_has_active(self):
        self.assertEqual(True, self.tag.active)

    def test_tag_has_reserve(self):
        self.assertEqual(False, self.tag.reserved)

    def test_reserved_is_reserved(self):
        self.assertEqual(True, self.reserved_tag.reserved)

    def test_colour_change(self):
        self.tag.change_colour(self.colour2)

        self.assertEqual(self.colour2, self.tag.colour)
    
    def test_tag_deactivate(self):
        self.tag.deactivate()
        self.assertEqual(False, self.tag.active)

    def test_tag_activate(self):
        self.tag.deactivate()
        self.tag.activate()
        self.assertEqual(True, self.tag.active)

    def test_cannot_deactivate_reserved(self):
        self.reserved_tag.deactivate()
        self.assertEqual(True, self.reserved_tag.active)