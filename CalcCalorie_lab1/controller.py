# Controlling work of program

import model
import view
import serialize


# Transfers all choices to model
# and model result to view, where result printing.
# Creating possibility to change cpnfig files and to dump some information
def main():
    while True:
        point = view.createMenu()
        if point == 1:
            gender = view.read_gender()
            weight = view.read_weight()
            height = view.read_height()
            age = view.read_age()
            pa = view.read_pa()
            calories = model.calculate_calories(
                gender, weight, height, age, pa)
            view.get_info(calories)
            data = (gender, weight, height, age, pa, calories)
            raw_input()
            if view.is_dump():
                serialize.dump(data)
        elif point == 2:
            serialize.load()
        elif point == 3:
            data = view.read_serialization_file()
            serialize.change_config(data[0], data[1])
        elif point == 4:
            break

main()
