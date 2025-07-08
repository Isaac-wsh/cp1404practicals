from guitar import Guitar

def main():
    """Load guitars from file, sort them by year, and display the list."""
    guitars = load_guitars("guitars.csv")
    guitars.sort()
    for guitar in guitars:
        print(guitar)

def load_guitars(filename):
    """Read guitars from file and return list of Guitar."""
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(",")
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitars.append(Guitar(name, year, cost))
    in_file.close()
    return guitars

main()
