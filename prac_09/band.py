class Band:
    def __init__(self, name = ""):
        """Initialise a Band with a name and musicians"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band"""
        self.musicians.append(musician)

