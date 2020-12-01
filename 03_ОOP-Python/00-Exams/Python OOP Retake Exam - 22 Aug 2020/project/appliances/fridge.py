from appliances.appliance import Appliance


class Fridge(Appliance):
    def __init__(self, cost: float = 1.2):
        super().__init__(cost)
