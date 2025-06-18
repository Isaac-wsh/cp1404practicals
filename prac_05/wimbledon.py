"""
Wimbledon
Estimate: 30 minutes
Actual:    minutes
"""

def main():
    filename = "wimbledon.csv"

def read_data(filename):
    """Read the file and return the champion and country"""
    import csv
    champions = []
    countries = set()
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.DictReader(in_file)
        for row in reader:
            champion = row["Champion"]
            country = row["Country"]
            champions.append(champion)
            countries.add(country)
    return champions, countries

def count_champions(champions):
    """Count the number of times each champion has won, sort the list, and return"""
    champion_counts = {}  # 普通字典
    for champion in champions:
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return sorted(champion_counts.items())