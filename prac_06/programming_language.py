"""
Estimate: 30 minutes
Actual:  20 minutes
"""

class ProgrammingLanguage:
    def __init__(self, language, typing, reflection, year):
        """Like most init functions, create the fields and set them to the parameters passed in"""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Returns True/False if the programming language is dynamically typed or not"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return the string"""
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"