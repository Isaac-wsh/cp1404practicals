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
            display_taxis(taxis)
            try:
                taxi_index = int(input("Choose taxi: "))
                if 0 <= taxi_index < len(taxis):
                    current_taxi = taxis[taxi_index]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input")
            print(f"Bill to date: ${total_bill:.2f}")
        elif choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    total_bill += trip_cost
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                except ValueError:
                    print("Invalid distance")
            print(f"Bill to date: ${total_bill:.2f}")
        else:
            print("Invalid option")
            print(f"Bill to date: ${total_bill:.2f}")

        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)

def display_taxis(taxis):
    """Display the list of taxis with their index."""
    print("Taxis available: ")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()