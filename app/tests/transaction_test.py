import unittest
from datetime import date
from app.models.colour import Colour
from app.models.tag import Tag
from app.models.merchant import Merchant
from app.models.transaction import Transaction

class TestTransaction(unittest.TestCase):

    def setUp(self):
        
        self.date = date.today()
        self.colour = Colour("black")
        self.tag1 = Tag("misc", self.colour)
        self.tag2 = Tag("misc2", self.colour)
        self.merchant1 = Merchant("tesco", self.tag1)
        self.transaction = Transaction(self.merchant1, 30.00, self.date)
        self.transaction2 = Transaction(self.merchant1, 30.00, self.date, self.tag2)

    def test_transaction_has_merchant(self):
        self.assertEqual(self.merchant1, self.transaction.merchant)

    def test_transaction_has_amount(self):
        self.assertEqual(30.00, self.transaction.amount)

    def test_transaction_has_date(self):
        self.assertEqual(self.date, self.transaction.date)

    def test_transaction_has_tag(self):
        self.assertEqual(self.tag1, self.transaction.tag)

    def test_transaction_has_non_default_tag(self):
        self.assertEqual(self.tag2, self.transaction2.tag)

