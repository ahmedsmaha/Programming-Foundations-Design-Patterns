from pizza import Pizza


class ThinPizza(Pizza):
    def __init__(self):
        self.description = "Thin pizza"

    def cost(self):
        return 1
