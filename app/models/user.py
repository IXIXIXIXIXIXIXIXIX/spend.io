from app.models.view_filter import ViewFilter

class User:

    def __init__(self, name, budget, remaining_budget = None, id=None):
        self.id = id
        self.name = name
        self.budget = budget
        if remaining_budget is not None:
            self.remaining_budget = remaining_budget
        else:
            self.remaining_budget = budget

        self.view_filter = ViewFilter()

    def register_spending(self, transaction):
        self.remaining_budget -= transaction.amount
        return self.remaining_budget

    def reset_budget(self):
        self.remaining_budget = self.budget

    def change_budget(self, new_budget):
        self.remaining_budget += (new_budget - self.budget)
        self.budget = new_budget
