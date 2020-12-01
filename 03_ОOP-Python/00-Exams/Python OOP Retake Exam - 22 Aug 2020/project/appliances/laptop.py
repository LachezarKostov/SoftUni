from appliances.appliance import Appliance


class Laptop(Appliance):
    def __init__(self, cost: float = 1):
        super().__init__(cost)