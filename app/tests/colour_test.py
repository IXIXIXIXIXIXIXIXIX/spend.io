import unittest
from app.models.colour import Colour 

class TestColour(unittest.TestCase):

    def setUp(self):
        self.colour = Colour("black")

    def test_colour_has_name(self):
        self.assertEqual("black", self.colour.colourname)