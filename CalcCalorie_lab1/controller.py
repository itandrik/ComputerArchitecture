# Controlling work of program

from model import Model
from view import View
from serialize import Serialize


# Transfers all choices to model
# and model result to view, where result printing.
# Creating possibility to change cpnfig files and to dump some information


class Controller:
    def __init__(self):
        self.view = View()
        self.serialize = Serialize()

    def menu(self):
        while True:
            point = self.view.create_menu()
            if point == 1:
                self._calculate()
            elif point == 2:
                self.serialize.load()
            elif point == 3:
                data = self.view.change_serialization_file()
                self.serialize.change_config(data[0], data[1])
            elif point == 4:
                break

    def _calculate(self):
        gender = self.view.read_gender()
        weight = self.view.read_weight()
        height = self.view.read_height()
        age = self.view.read_age()
        pa = self.view.read_pa()
        model = Model(gender, weight, height, age, pa)
        calories = model.calculate_calories()
        self.view.get_info(calories)
        data = (gender, weight, height, age, pa, calories)
        input()
        if self.view.is_dump():
            self.serialize.dump(data)
