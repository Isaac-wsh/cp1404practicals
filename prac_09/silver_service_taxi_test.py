from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Create a SilverServiceTaxi with fanciness = 2"""
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.start_fare()
    taxi.drive(18)
    print(taxi)
    fare = taxi.get_fare()
    print(f"Fare: ${fare:.2f}")
    assert abs(fare - 48.80) < 0.01, f"Expected $48.78 but got ${fare:.2f}"
main()