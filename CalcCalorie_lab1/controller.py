# Controlling work of program

from model import Model
from view import View
<<<<<<< HEAD
from serialize import Serialize
=======
import serialize
>>>>>>> d99509dc60f8acc45727943d2fbec84dc766b4d2


# Transfers all choices to model
# and model result to view, where result printing.
# Creating possibility to change cpnfig files and to dump some information


class Controller:
    def __init__(self):
        self.view = View()
<<<<<<< HEAD
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
=======

    def menu(self):
        while True:
            point = self.view
            if point == 1:
                self._calculate()
            elif point == 2:
                serialize.load()
            elif point == 3:
                data = self.view.change_serialization_file()
                serialize.change_config(data[0], data[1])
>>>>>>> d99509dc60f8acc45727943d2fbec84dc766b4d2
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
<<<<<<< HEAD
        self.view.get_info(calories)
        data = (gender, weight, height, age, pa, calories)
        raw_input()
        if self.view.is_dump():
            self.serialize.dump(data)
=======
        self.view.get_info()
        data = (gender, weight, height, age, pa, calories)
        raw_input()
        if self.view.is_dump():
            serialize.dump(data)
>>>>>>> d99509dc60f8acc45727943d2fbec84dc766b4d2
