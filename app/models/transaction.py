from datetime import date

class Transaction:

    def __init__(self, merchant, amount, date, tag = None, id = None):

        self.amount = amount
        self.merchant = merchant
        self.date = date

        if tag is None:
            self.tag = merchant.default_tag
        else:
            self.tag = tag


