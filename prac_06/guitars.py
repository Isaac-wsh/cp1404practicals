from guitar import Guitar

def main():
    """Use Guitar class"""
    print("My guitars!")
    guitars = []
    # name = input("Name: ")
    # while name != "":
    #     year = int(input("Year: "))
    #     cost = float(input("Cost: "))
    #     guitar = Guitar(name, year, cost)
    #     guitars.append(guitar)
    #     print(guitar, "added")
    #     name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            else:
                vintage_string = ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()

