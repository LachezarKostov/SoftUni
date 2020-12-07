class Room:
    family_name: str
    budget: float
    members_count: int

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, val):
        if val < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = val

    def calculate_expenses(self, *args):
        self.expenses = sum(el.cost for seq in args for el in seq)

    @property
    def cost(self):
        return self.expenses * 30 + self.room_cost

    def __str__(self):
        return "\n".join([
             f"{self.family_name} with {self.members_count} member. Budget: {self.budget:.2f}$, Expenses: {self.expenses * 30:.2f}"
         ] + [
             f"--- Child {idx + 1} monthly cost: {c.cost * 30}$" for idx, c in enumerate(self.children)
         ] + [
             f"--- Appliances monthly cost: {sum(app.get_monthly_expense() for app in self.appliances)}$"
         ])
