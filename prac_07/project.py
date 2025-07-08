"""
Estimate: 40 minutes
Actual:   minutes
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

