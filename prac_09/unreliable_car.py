from prac_09.car import Car
import random

class UnreliableCar(Car):
    """Make our own derived class for an UnreliableCar that inherits from Car"""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car"""
        random_chance = random.uniform(0, 100)
        if random_chance < self.reliability:
            return super().drive(distance)
        else:
            return 0