class Room:
    family_name: str
    budget: float
    members_count: int

    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self._expenses = 0

    @property
    def calculate_expenses(self):
        return self._expenses

    @calculate_expenses.setter
    def calculate_expenses(self, *args):
        total_cost = sum([x.cost for x in args])
        if total_cost < 0:
            raise ValueError("Expenses cannot be negative")

        self._expenses = total_cost

