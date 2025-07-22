from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with name, fuel, and a new attribute fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Calculate the fare."""
        base_fare = super().get_fare()
        return base_fare + self.flagfall

    def __str__(self):
        """Return a string representation of the SilverServiceTaxi."""
        base_str = super().__str__()
        return f"{base_str} plus flagfall of ${self.flagfall:.2f}"