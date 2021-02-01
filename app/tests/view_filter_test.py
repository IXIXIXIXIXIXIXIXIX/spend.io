import unittest
from datetime import date
from app.models.colour import Colour
from app.models.tag import Tag
from app.models.merchant import Merchant
from app.models.transaction import Transaction
from app.models.view_filter import ViewFilter

class TestViewFilter(unittest.TestCase):

    def setUp(self):
        self.date = date.today()
        self.colour = Colour("black")
        self.tag1 = Tag("misc", self.colour)
        self.merchant1 = Merchant("tesco", self.tag1)
        self.transaction = Transaction(self.merchant1, 30.00, self.date)
        self.view_filter = ViewFilter()

    def test_filter_is_inactive(self):
        self.assertEqual(False, self.view_filter.filter_active)

    def test_filter_add_tag(self):
        self.view_filter.add_tag(self.tag1)

        self.assertEqual(True, self.view_filter.filter_active)
        self.assertEqual(1, len(self.view_filter.tag_ids))
    
    def test_filter_remove_tag(self):
        self.view_filter.add_tag(self.tag1)
        self.assertEqual(True, self.view_filter.filter_active)
        self.assertEqual(1, len(self.view_filter.tag_ids))

        self.view_filter.remove_tag(self.tag1)
        self.assertEqual(False, self.view_filter.filter_active)
        self.assertEqual(0, len(self.view_filter.tag_ids))

    def test_filter_add_merchant(self):
        self.view_filter.add_merchant(self.merchant1)

        self.assertEqual(True, self.view_filter.filter_active)
        self.assertEqual(1, len(self.view_filter.merchant_ids))
    
    def test_filter_remove_merchant(self):
        self.view_filter.add_merchant(self.merchant1)
        self.assertEqual(True, self.view_filter.filter_active)
        self.assertEqual(1, len(self.view_filter.merchant_ids))

        self.view_filter.remove_merchant(self.merchant1)
        self.assertEqual(False, self.view_filter.filter_active)
        self.assertEqual(0, len(self.view_filter.merchant_ids))

    def test_deactivate_filter(self):
        self.view_filter.add_merchant(self.merchant1)
        self.assertEqual(True, self.view_filter.filter_active)
        self.assertEqual(1, len(self.view_filter.merchant_ids))

        self.view_filter.deactivate_filter()
        self.assertEqual(False, self.view_filter.filter_active)

    def test_reactivate_filter(self):
        self.view_filter.add_merchant(self.merchant1)
        self.assertEqual(True, self.view_filter.filter_active)
        self.assertEqual(1, len(self.view_filter.merchant_ids))

        self.view_filter.deactivate_filter()
        self.assertEqual(False, self.view_filter.filter_active)
        self.view_filter.activate_filter()
        self.assertEqual(True, self.view_filter.filter_active)

    def test_clear_filter(self):
        self.view_filter.add_tag(self.tag1)
        self.assertEqual(True, self.view_filter.filter_active)
        self.assertEqual(1, len(self.view_filter.tag_ids))

        self.view_filter.add_merchant(self.merchant1)
        self.assertEqual(1, len(self.view_filter.merchant_ids))

        self.view_filter.clear()

        self.assertEqual(0, len(self.view_filter.merchant_ids))
        self.assertEqual(0, len(self.view_filter.tag_ids))
        self.assertEqual(False, self.view_filter.filter_active)