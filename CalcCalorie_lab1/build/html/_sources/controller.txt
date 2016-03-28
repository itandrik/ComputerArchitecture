AUTO-GENERATED DOCUMENTATION
=============================
# Controlling work of program

import model
import view


# Transfers all choices to model
# and model result to view, where result printing
def main():
    while(True):
        view.createMenu()
        try:
            point = input()
            if(point == 1):
                gender = view.readGender()
                weight = view.readWeight()
                height = view.readHeight()
                age = view.readAge()
                pa = view.readPA()
                view.getInfo(model.calculate_calories(gender, weight, height, age, pa))
                raw_input()
            elif(point == 2):
                break
            else:
                print("Wrong input! Try again")
        except NameError:
            print ("Wrong input! Try again")

main()

