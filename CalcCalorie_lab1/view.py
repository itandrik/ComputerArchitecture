import global_koefs
# Printing all points to
# choose to calculate calories


class View:
    # Printing menu of age choice
    def read_age(self):
        while True:
            try:
                age = eval(input("Age: "))
                if age >= 13 & age < 80:
                    break
                else:
                    print("Unreal age!")
                    print("Repeat please, age should be between 13 and 80")
            except (NameError, SyntaxError):
                print("Wrong input! Repeat please")
        return age

    # Printing menu of gender choice
    def read_gender(self):
        while True:
            for i in global_koefs.str1:
                print (i)
            try:
                gender = eval(input())
                if ((gender > 0) & (gender < 3)):
                    break
                else:
                    print("Wrong input! Repeat please")
            except (NameError, SyntaxError):
                print("Wrong input! Repeat please")
        return gender

    # Printing menu of weight choice
    def read_weight(self):
        while True:
            try:
                weight = eval(input("Weight: "))
                if ((weight >= 35) & (weight < 250)):
                    break
                else:
                    print("Repeat please, weight should be between 35 and 250")
            except (NameError, SyntaxError):
                print("Wrong input! Repeat please")
        return weight

    # Printing menu of height choice
    def read_height(self):
        while True:
            try:
                height = eval(input("Height in cm: "))
                if ((height >= 120) & (height < 250)):
                    break
                else:
                    print("Repeat please,"
                          " height should be between 120 and 250")
            except (NameError, SyntaxError):
                print("Wrong input! Repeat please")
        return height

    # Printing menu of physical activity choice
    def read_pa(self):
        while True:
            for i in global_koefs.str2:
                print (i)
            try:
                pa = eval(input())
                if ((pa >= 1) & (pa <= 5)):
                    break
                else:
                    print("Wrong input! Repeat please...")
            except (NameError, SyntaxError):
                print("Wrong input! Repeat please")
        return pa

    # Printing main menu
    def create_menu(self):
        while True:
            for i in global_koefs.str3:
                print (i)
            try:
                point = eval(input())
                if ((point >= 1) & (point <= 4)):
                    return point
                else:
                    print("Wrong input! Try again")
            except (NameError, SyntaxError):
                print ("Wrong input! Try again")

    # Printing menu for choosing type of serialization
    def read_serialization_type(self):
        s_type = 0
        while True:
            for i in global_koefs.str4:
                print (i)
            try:
                s_type = eval(input())
                if ((s_type >= 1) & (s_type <= 3)):
                    break
                else:
                    print("Wrong input! Repeat please...")
            except (NameError, SyntaxError):
                print("Wrong input! Repeat please")
        if s_type == 1:
            return 'pickle'
        elif s_type == 2:
            return 'json'
        else:
            return 'yaml'

    # Checking dump function
    # return boolean
    def is_dump(self):
        while True:
            for i in global_koefs.str5:
                print (i)
            try:
                inp = eval(input())
                if inp == 1:
                    return True
                elif inp == 2:
                    return False
                else:
                    print("Wrong input! Repeat please...")
            except (NameError, SyntaxError):
                print("Wrong input! Repeat please")

    # Printing menu, where user can change
    #  type of serialization and dump filename
    def change_serialization_file(self):
        inp = input("Enter your file name(without file format) : ")
        return self.read_serialization_type(), inp

    # Printing result of program
    def get_info(self, str):
        print (str)
