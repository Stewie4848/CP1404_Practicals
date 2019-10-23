from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    reliability = 50

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, fuel={}".format(self.name, self.fuel)

    def drive(self, distance):
        number = randint(0, 100)
        if number < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            return distance
        else:
            return 0
