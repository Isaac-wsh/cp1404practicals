"""
Estimate: 40 minutes
Actual:   minutes
"""

import datetime


class Project:
    """Used to represent data of project class"""

    def __int__(self, name, start_time, priority, estimate, completion):
        """Initialize the project object"""
        self.name = name
        self.start_time = start_time
        self.priority = int(priority)
        self.estimate = float(estimate)
        self.completion = int(completion)
