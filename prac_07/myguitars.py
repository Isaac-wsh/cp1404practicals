from guitar import Guitar

def main():

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
