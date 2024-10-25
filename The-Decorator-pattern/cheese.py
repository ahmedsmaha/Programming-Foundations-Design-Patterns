from topping_decorator import ToppingDecorator


class Cheese(ToppingDecorator):

    def __init__(self, pizza):
        self.pizza = pizza

    def get_description(self):
        return self.pizza.get_description() + ", cheese"

    def cost(self):
        return self.pizza.cost() + 0.5
