from datetime import datetime


class Task:
    """Class to describe task entity"""
    def __init__(self, name, date, description=""):
        self.name = name
        self.date = datetime.strptime(date, "%d-%m-%Y %H:%M")
        self.description = description

    def __repr__(self):
        return "<%s, %s>" % (str(self.date), self.name)

# List that contains user's tasks
list_of_tasks = []
