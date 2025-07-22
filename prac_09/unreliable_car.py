from prac_09.car import Car

class UnreliableCar(Car):
    """Make our own derived class for an UnreliableCar that inherits from Car"""
    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability