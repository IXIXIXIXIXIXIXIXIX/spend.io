from datetime import date

class Transaction:

    def __init__(self, merchant, amount, date, tag = None, id = None):

        self.amount = amount
        self.merchant = merchant
        self.date = date
        self.id = id

        if tag is None:
            self.tag = merchant.default_tag
        else:
            self.tag = tag

    def change_tag(self, tag):
        self.tag = tag

    def to_default_tag(self):
        self.change_tag(self.merchant.default_tag)

