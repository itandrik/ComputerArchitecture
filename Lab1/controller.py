from model import Task
import view


# Function to add tasks
def add_task_(list_of_tasks, name, description, date):
    try:
        list_of_tasks.append(Task(name, date, description))
    except ValueError:
        print("Incorrect date")


# Function to edit tasks
def edit_(list_of_tasks, number, new_name, new_description, new_date):
    list_of_tasks[number].name = new_name
    list_of_tasks[number].description = new_description
    list_of_tasks[number].date = new_date


# Function to remove tasks
def remove_(list_of_tasks):
    view.output_by_adding_date()
    number = input("Enter number of task, which you want to remove: ")
    list_of_tasks.pop(int(number))


# Function to sort tasks by name
def by_name(task):
    """testing by_name
    >>> by_name(Task("buy bred", "12-12-1212 14:15", "des"))
    'buy bred'
    """
    return task.name


# Function to sort tasks by date
def by_date(task):
    """
    testing by_name
    >>> by_name(Task("buy bred", "12-12-1212 13:15", "des"))
    'buy bred'
    """
    return task.des

if __name__ == "__main__":
    import doctest
    doctest.testmod()