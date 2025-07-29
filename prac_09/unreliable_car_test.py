from prac_09.unreliable_car import UnreliableCar

def main():
    """Create an unreliable car"""
    my_car = UnreliableCar("Car", 100, 30)
    for i in range(1, 101):
        distance = my_car.drive(10)
        print(f"Attempt {i}: Tried to drive 10km — actually drove {distance}km")
main()
