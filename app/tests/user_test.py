import unittest
from datetime import date
from app.models.user import User
from app.models.colour import Colour
from app.models.tag import Tag
from app.models.merchant import Merchant
from app.models.transaction import Transaction


class TestUser(unittest.TestCase):

    def setUp(self):
        self.date = date.today()
        self.user = User("Scott", 100.00)
        self.colour = Colour("black")
        self.tag = Tag("misc", self.colour)
        self.merchant = Merchant("tesco", self.tag)
        self.transaction = Transaction(self.merchant, 10.00, self.date)

    def test_user_has_name(self):
        self.assertEqual("Scott", self.user.name)

    def test_user_has_budget(self):
        self.assertEqual(100.00, self.user.budget)
    
    def test_user_has_remaining_budget(self):
        self.assertEqual(100.00, self.user.remaining_budget)

    def test_user_register_spend(self):
        self.user.register_spending(self.transaction)
        self.assertEqual(90.00, self.user.remaining_budget)

    def test_user_reset_budget(self):
        self.user.register_spending(self.transaction)
        self.assertEqual(90.00, self.user.remaining_budget)
        
        self.user.reset_budget()
        self.assertEqual(100.00, self.user.remaining_budget)

    def test_user_change_budget(self):
        self.user.register_spending(self.transaction)
        self.assertEqual(90.00, self.user.remaining_budget)

        self.user.change_budget(110.00)

        self.assertEqual(110.00, self.user.budget)
        self.assertEqual(100.00, self.user.remaining_budget)