class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """With defaults name="", year=0, cost=0"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Use {} string formatting to return the sentence"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Returns how old the guitar is in years"""
        current_year = 2025
        age = current_year - self.year
        return age

    def is_vintage(self):
        """Determining if a guitar is 50 years old or older"""
        if self.get_age() >= 50:
            return True
        else:
            return False

