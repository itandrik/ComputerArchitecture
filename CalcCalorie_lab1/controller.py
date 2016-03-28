# Обробіток запросів користувача і виклик існуючих ресурсів
import model
import view


def main():
    while(True):
        view.createMenu()
        point = input()
    if(point == 1):
            gender = view.readGender()
            weight = view.readWeight()
            height = view.readHeight()
            age = view.readAge()
            pa = view.readPA()
            model.calculate_calories(gender, weight, height, age, pa)
    elif(point == 2):
        break
    else:
        print("Wrong input! Try again")

main()
