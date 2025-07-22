from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50
    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi with name, fuel, and a new attribute fanciness."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness