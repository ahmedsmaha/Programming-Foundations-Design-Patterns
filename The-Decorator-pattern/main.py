import pprint
from thin_pizza import ThinPizza
from thick_pizza import ThickPizza
from cheese import Cheese
from olive import Olive

if __name__ == '__main__':
    pizza = ThinPizza()
    pizza_and_cheese = Cheese(pizza)
    pizza_and_olive = Olive(pizza)
    pizza_and_cheese_olive = Olive(pizza_and_cheese)
    print(pizza.cost(), pizza.get_description())
    print(pizza_and_cheese.cost(), pizza_and_cheese.get_description())
    print(pizza_and_olive.cost(), pizza_and_olive.get_description())
    print(pizza_and_cheese_olive.cost(),
          pizza_and_cheese_olive.get_description())
