class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """With defaults name="", year=0, cost=0"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Use {} string formatting to return the sentence"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"