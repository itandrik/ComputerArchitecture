from BloodPressure.Globals.globals import *


# class View. It writes some new information and input from user
class View:
    def create_menu(self):
        for point in menu_str:
            print(point)
        try:
            point = eval(input())
            if ((point >= 1) & (point <= 13)):
                return point
            else:
                print("Wrong input! Try again")
        except (NameError, SyntaxError):
            print("Wrong input! Try again")

    def get_info(self, data_array, table_name):
        i = 0
        print("ID: "+data_array[i])
        i+=1
        for point in table_data[table_name]:
            print(point+": "+data_array[i])
            i+=1
