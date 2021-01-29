class User:

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
        self.remaining_budget = budget

    def register_spending(amount):
        self.remaining_budget -= amount
        return self.remaining_budget

    def reset_budget():
        self.remaining_budget = budget

    def change_budget(new_budget):
        self.remaining_budget += (new_budget - self.budget)
        self.budget = new_budget
