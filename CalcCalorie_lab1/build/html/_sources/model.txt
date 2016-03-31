 # Creating model. Describing functions,
# which calculate calories, using human parameters

"""
Testing module :
Calculating physical activity procedure :
>>> calculate_pa(1)
1.2
>>> calculate_pa(2)
1.375
>>> calculate_pa(3)
1.4625
>>> calculate_pa(4)
1.6375
>>> calculate_pa(5)
1.725
Calculating calories :
>>> calculate_calories(1,54,165,18,1)
1799.277
>>> calculate_calories(1,73,187,19,2)
2534.01225
>>> abs(calculate_calories(2,65,178,20,2)-2072.10)<1e-2
True
"""


# Calculating index of physical activity
def calculate_pa(pa):
    if pa == 1:
        return 1.2
    elif pa == 2:
        return 1.375
    elif pa == 3:
        return 1.4625
    elif pa == 4:
        return 1.6375
    elif pa == 5:
        return 1.725


# Calculating calories, which spend person per day
def calculate_calories(gender, weight, height, age, pa):

    # Calculating with Harris-Benedict formula
    if gender == 1:
        calories1 = 66.5 + (13.75 * weight) + (5.003 * height) - (6.775 * age)
    else:
        calories1 = 655.1 + (9.563 * weight) + (1.85 * height) - (4.676 * age)

    # Calculating with Muffin-Jeor formula
    if gender == 1:
        calories2 = 5 + (10*weight) + (6.25 * height) - (5 * age)
    else:
        calories2 = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # Average value for more accuracy value
    return calculate_pa(pa) * ((calories1 + calories2) / 2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
