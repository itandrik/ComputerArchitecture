# Controlling work of program

import model
import view
import serialize

# Transfers all choices to model
# and model result to view, where result printing
def main():
    while True:
        point = view.createMenu()
        if point == 1:
            gender = view.readGender()
            weight = view.readWeight()
            height = view.readHeight()
            age = view.readAge()
            pa = view.readPA()
            calories = model.calculate_calories(
                gender, weight, height, age, pa)
            view.getInfo(calories)
            data = (gender, weight, height, age, pa, calories)
            raw_input()
            if view.isDump(): serialize.dump(data)
        elif point == 2:
            serialize.load()
        elif point == 3:
            data = view.changeSerializationFile()
            serialize.change_config(data[0],data[1])
        elif point == 4:
            break

main()
 