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