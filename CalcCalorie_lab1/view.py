str1 = ["Gender:","1.Male","2.Female"];
str2 = ["Physical activity:", "1.Minimum physical activity", "2. 3 times per week", "3. 5 times per week", "4. Every day",
        "5. 2 times per day"];

def readAge():
    while(True):
        age = input("Age: ")
        if(age.isdigit()&(age>=13)&(age<=80)):
            break
        else:
            print("Unreal age! Repeat please, age should be between 13 and 80")
    return age

def readGender():
    while(True):
        for i in str1:
            print i
        gender = input()
        if(gender.isdigit()&(gender>0)&(gender<3)):
            break
        else:
            print("Wrong input! Repeat please")
    return gender

def readWeight():
    while(True):
        weight = input("Weight: ")
        if(weight.isdigit()&(weight>=35)&(weight<250)):
            break
        else:
            print("Wrong input! Repeat please, weight should be between 35 and 250")
    return weight

def readHeight():
    while(True):
        height = input("Height in cm: ")
        if(height.isdigit()&(height>=120)&(height<250)):
            break
        else:
            print("Wrong input! Repeat please, height should be between 120 and 250")
    return height

def readPA():
    while(True):
        for i in str2:
            print i
        pa = input()
        if(pa.isdigit()&(pa>=1)&(pa<=5)):
            break
        else:
            print("Wrong input! Repeat please...")
    return pa
