from view import View
from BloodPressure.Config.config_parser import ConfigParser

table_data = {
    "pressure_data": ("date", "time", "upper level", "lower level", "pulse", "person_id_person", "doctor_id_doctor"),
    "person": ("first name", "last name", "middle name", "age", "weight", "height", "phone_number"),
    "doctor": ("first name", "last name", "middle name", "profession", "phone number")
}
operations = {
    0: "load",
    1: "add",
    2: "delete",
    3: "change",
    4: "config"
}
tables = {
    0: "person",
    1: "doctor",
    2: "pressure_data"
}
databases = ("mysql", "sqlite", "postgreSQL")

class Controller:
    def __init__(self):
        self.view = View()
        self.config = ConfigParser()

    def main(self):
        while True:
            point = self.view.create_menu()
            self.handler(operations[int(point//3)],tables[(point-1)%3])

    def handler(self, operation, table_name):
        if operation == "load":
            id = input("Enter id")
            model.load(table_name,id)
        elif operation == "add":
            data = []
            for i in table_data[table_name]:
                point = input("Enter" + i)
                data.append(point)
            model.insert(table_name,data)
        elif operation == "change":
            data = []
            id = input("Enter id")
            for i in table_data[table_name]:
                point = input("Enter" + i)
                data.append(point)
            model.update(table_name, data)
        elif operation == "delete":
            id = input("Enter id")
            model.delete(table_name, id)
        elif operation=="config":
            for i in range(1, 4):
                print("%d. %s" % (i, databases[i - 1]))
            point = input()
            self.config.change_config(databases[point - 1])

