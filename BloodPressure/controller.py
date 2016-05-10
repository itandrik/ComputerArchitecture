from view import View
from BloodPressure.Work_with_db.db import SqlWorker
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
    3: "change"
}
tables = {
    0: "person",
    1: "doctor",
    2: "pressure_data"
}
class Controller:
    def __init__(self):
        self.view = View()

    def main(self):
        while True:
            point = self.view.create_menu()
            self.handler(operations[int(point//4)],tables[(point-1)%3])

    def handler(self, operation, table_name):
        if operation == "load":
            id = input("Enter id")
            self.sql_worker.load(table_name,id)
        elif operation == "add":
            data = []
            for i in table_data[table_name]:
                point = input("Enter" + i)
                data.append(point)
            self.sql_worker.insert(table_name,data)
        elif operation == "change":
            data = []
            id = input("Enter id")
            for i in table_data[table_name]:
                point = input("Enter" + i)
                data.append(point)
            self.sql_worker.update(table_name, data)
        elif operation == "delete":
            id = input("Enter id")
            self.sql_worker.delete(table_name, id)
