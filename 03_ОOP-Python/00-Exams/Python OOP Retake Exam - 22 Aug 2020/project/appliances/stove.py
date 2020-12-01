from appliances.appliance import Appliance


class Stove(Appliance):
    def __init__(self, cost: float = 0.7):
        super().__init__(cost)
