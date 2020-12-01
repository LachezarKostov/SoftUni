class Appliance:
    def __init__(self, cost: float):
        self.cost = cost
        # The cost is for a single day
        self.DAYS_IN_MONTH = 30

    def get_monthly_expense(self):
        cost_for_month = self.DAYS_IN_MONTH * self.cost
        return cost_for_month
