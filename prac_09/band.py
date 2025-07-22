class Band:
    def __init__(self, name = ""):
        """Initialise a Band with a name and musicians"""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band"""
        self.musicians.append(musician)

    def __str__(self):
        """Return the string"""
        member = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({member})"

    def play(self):
        """Return a string of musicians."""
        return "\n".join(musician.play() for musician in self.musicians)