import model
import controller
import pickle


# Function to print list sorted by adding date
def output_by_adding_date():
    for index, item in enumerate(model.list_of_tasks):
        print(index, item)


# Function to print list sorted by name
def output_by_name():
    for item in sorted(model.list_of_tasks, key=controller.by_name):
        print(item)


# Function to print list sorted by date
def output_by_date():
    for item in sorted(model.list_of_tasks, key=controller.by_date):
        print(item)


# Function to output task list with description
def output_with_description():
    for index in model.list_of_tasks:
        print("<%s, %s> - %s" % (index.date, index.name, index.description))


def add_task():
    name = input("Enter name of your task: ")
    date = input("Enter date of your task: ")
    description = input("Enter description for your task: ")
    controller.add_task_(model.list_of_tasks, name, date, description)


def edit():
    output_by_adding_date()
    number = input("Enter number of task, which you want to edit: ")
    new_name = input("Enter new name for your task: ")
    new_date = input("Enter new date for your task: ")
    new_description = input("Enter new description for your task: ")
    controller.edit_(model.list_of_tasks, int(number), new_name, new_date, new_description)


def remove():
    output_by_adding_date()
    number = input("Enter number of task, which you want to remove: ")
    controller.remove_(int(number))


# Function to print main menu
def print_main_menu():
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Edit Task")
    print("4. Print list sorted by name")
    print("5. Print list sorted by date")
    print("6. Print list sorted by adding date")
    print("7. Print tasks list with description")
    print("8. Exit")
    print("\nEnter number")


# Function to menu selection and call the respective function
def menu():
    try:
        f1 = open('tasks.txt', "rb")
        model.list_of_tasks = pickle.load(f1)
    except IOError:
        f1 = open('tasks.txt', "wb")
    f1.close()

    flag = False
    while not flag:
        print_main_menu()
        x = input()
        if x == '1':
            add_task()
        elif x == '2':
            remove()
        elif x == '3':
            edit()
        elif x == '4':
            output_by_name()
            input()
        elif x == '5':
            output_by_date()
            input()
        elif x == '6':
            output_by_adding_date()
            input()
        elif x == '7':
            output_with_description()
            input()
        elif x == '8':
            flag = True

    f1 = open('tasks.txt', 'wb')
    pickle.dump(model.list_of_tasks, f1)
    f1.close()
