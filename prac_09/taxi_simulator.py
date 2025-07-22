from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Call Taxi and SilverServiceTaxi and output the results"""
    print("Let's drive!")
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0.0
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":


def display_taxis(taxis):
    """Display the list of taxis with their index."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")