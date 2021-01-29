import unittest
from app.models.colour import Colour
from app.models.tag import Tag
from app.models.merchant import Merchant

class TestMerchant(unittest.TestCase):

    def setUp(self):

        self.colour = Colour("black")
        self.tag1 = Tag("misc", self.colour)
        self.tag2 = Tag("misc2", self.colour)
        self.inactive_tag = Tag("general", self.colour, False)
        self.merchant = Merchant("Tesco", self.tag1)
    

    def test_merchant_has_name(self):
        self.assertEqual("TESCO", self.merchant.name)

    def test_merchant_has_default_tag(self):
        self.assertEqual(self.tag1, self.merchant.default_tag)

    def test_merchant_is_active(self):
        self.assertEqual(True, self.merchant.active)

    def test_merchant_deactivate(self):
        self.merchant.deactivate()
        self.assertEqual(False, self.merchant.active)

    def test_merchant_reactivate(self):
        self.merchant.deactivate()
        self.assertEqual(False, self.merchant.active)

        self.merchant.activate()
        self.assertEqual(True, self.merchant.active)

    def test_change_default_tag(self):
        self.merchant.change_default(self.tag2)
        self.assertEqual(self.tag2, self.merchant.default_tag)

    def test_change_tag_inactive(self):
        self.merchant.change_default(self.inactive_tag)

        self.assertEqual(self.tag1, self.merchant.default_tag)