activity_dict = {1: 1.2,
                  2: 1.375,
                  3: 1.4625,
                  4: 1.6375,
                  5: 1.725
                }
coef = {
    'HB' :{
        True: (66.5, 13.75, 5.003, -6.775),
        False:(655.1, 9.563, 1.85, -4.676)
    },
    'MJ':{
        True: (5, 10, 6.25, -5),
        False: (-161, 10, 6.25, -5)
    }
}
str1 = ("Gender:", "1.Male", "2.Female")
str2 = ("Physical activity:", "1.Minimum physical activity",
             "2. 3 times per week", "3. 5 times per week",
             "4. Every day", "5. 2 times per day")
str3 = ("1. Calculate your calories", "2. Get results from file",
             "3. Change configuration file", "4. Exit")
str4 = ("1.Pickle", "2. JSON", "3.YAML")
str5 = ("Do you want to write your result into the file?",
             "1.Yes",
             "2. No")
gender_coefs = {True : 'Male', False : 'Female'}