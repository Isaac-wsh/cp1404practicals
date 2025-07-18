"""
Estimate: 2 hours
Actual: 6 hours
"""

from datetime import datetime

class Project:
    """Used to represent data of project class"""

    def __init__(self, name, start_time, priority, estimate, completion):
        """Initialize the project object"""
        self.name = name
        self.start_time = datetime.strptime(start_time, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.estimate = float(estimate)
        self.completion = int(completion)

    def __str__(self):
        """Return a string representation of the project"""
        return (f"{self.name}, start: {self.start_time.strftime("%d/%m/%Y")},"
                f"priority {self.priority}, estimate:${self.estimate:.2f},"
                f"completion:{self.completion}%")

    def __lt__(self, other):
        """Automatically sort Project objects by priority"""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion == 100

# p1 = Project("A", "01/01/2024", 1, 100.0, 50)
# p2 = Project("B", "01/01/2024", 3, 100.0, 50)
#
# print(p1)
# print(p2)
# print(p1 < p2)

