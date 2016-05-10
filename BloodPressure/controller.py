from view import View
from BloodPressure.Work_with_db.db import *
from BloodPressure.Config.config_parser import MyConfigParser
from BloodPressure.Globals.globals import *


class Controller:
    def __init__(self):
        self.view = View()
        self.config = MyConfigParser()
        self.sql_worker = SqlWorker(self.config.read_config())

    def main(self):
        try:
            while True:
                point = self.view.create_menu()
                self.handler(operations[int((point-1) / 3)],
                             tables[(point-1) % 3])
                input()
        except TypeError:
            self.view.show_exit()

    def handler(self, operation, table_name):
        if operation == "load":
            if table_name == "pressure_data":
                id = input("Enter id")
                self.view.get_info(
                    self.sql_worker.load(table_name, id),
                    table_name
                )
            else:
                self.view.get_info(
                    self.sql_worker.load(table_name),
                    table_name
                )
        elif operation == "add":
            data = []
            for i in table_data[table_name]:
                point = input("Enter " + i + " : ")
                data.append(point)
            self.sql_worker.insert(table_name, data)
        elif operation == "change":
            data = []
            id = input("Enter id")
            for i in table_data[table_name]:
                point = input("Enter " + i + " : ")
                data.append(point)
            self.sql_worker.update(table_name, id, data)
        elif operation == "delete":
            id = input("Enter id")
            self.sql_worker.delete(table_name, id)
        elif operation == "config":
            for i in range(1, 4):
                print("%d. %s" % (i, databases[i - 1]))
            point = input()
            self.config.change_config(databases[int(point) - 1])
            self.sql_worker = SqlWorker(self.config.read_config())
