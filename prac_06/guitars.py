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
    if len(guitars) > 0:
        print("These are my guitars:")
        i = 1
        for guitar in guitars:
            if guitar.is_vintage():
                vintage = " (vintage)"
            else:
                vintage = ""
            print("Guitar " + str(i) + ": " + guitar.name + " (" + str(guitar.year) + "), worth $" + str(round(guitar.cost, 2)) + vintage)
            i += 1

main()

