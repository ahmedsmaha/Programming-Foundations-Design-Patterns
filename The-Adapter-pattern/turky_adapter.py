from duck import Duck


class TurkyAdapter(Duck):

    def __init__(self, turky):
        self.__turky = turky

    def fly(self):
        self.__turky.fly()

    def quack(self):
        self.__turky.gobble()
