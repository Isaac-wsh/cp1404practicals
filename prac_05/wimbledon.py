"""
Wimbledon
Estimate: 30 minutes
Actual:    minutes
"""

def main():
    filename = "wimbledon.csv"
    champions, countries = read_data(filename)
    champion_data = count_champions(champions)
    display_champions(champion_data)
    display_countries(countries)

def read_data(filename):
    """Read the file and return the champion and country"""
    champions = []
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()[1:]
        for line in lines:
            parts = line.strip().split(",")
            country = parts[1]
            champion = parts[2]
            champions.append(champion)
            countries.add(country)
    return champions, countries

def count_champions(champions):
    """Count the number of times each champion has won, sort the list, and return"""
    champion_counts = {}
    for champion in champions:
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return sorted(champion_counts.items())

def display_champions(champion_data):
    """Print champion and number of wins"""
    print("Wimbledon Champions:")
    for name, count in champion_data:
        print(f"{name} {count}")

def display_countries(countries):
    """Print the winning countries and sort them"""
    sorted_countries = sorted(countries)
    print(f"\nThese {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))

main()
