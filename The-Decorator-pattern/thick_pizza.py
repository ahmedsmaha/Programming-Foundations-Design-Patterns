from pizza import Pizza


class ThickPizza(Pizza):
    def __init__(self):
        self.description = "Thick pizza"

    def cost(self):
        return 1.5
