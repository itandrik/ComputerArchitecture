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
import view


class Model:
    def __init__(self, gender, weight, height, age, pa):
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age
        self.pa = pa

    # Calculating index of physical activity
    def _calculate_pa(self):
        if self.pa == 1:
            return 1.2
        elif self.pa == 2:
            return 1.375
        elif self.pa == 3:
            return 1.4625
        elif self.pa == 4:
            return 1.6375
        elif self.pa == 5:
            return 1.725

    # Calculating calories, which spend person per day
    def calculate_calories(self):
        # Calculating with Harris-Benedict formula
        if self.compare():
            calories1 = 66.5 + (13.75 * self.weight) + (5.003 * self.height) - (6.775 * self.age)
        else:
            calories1 = 655.1 + (9.563 * self.weight) + (1.85 * self.height) - (4.676 * self.age)

        # Calculating with Muffin-Jeor formula
        if self.compare():
            calories2 = 5 + (10 * self.weight) + (6.25 * self.height) - (5 * self.age)
        else:
            calories2 = (10 * self.weight) + (6.25 *self. height) - (5 * self.age) - 161

        # Average value for more accuracy value
        return self._calculate_pa() * ((calories1 + calories2) / 2)

    def compare(self):
        if (self.gender == 1):
            return True
        else:
            return False

    def get_info(self):
        if (self.compare()):
            gender = 'male'
        else:
            gender = 'female'
        print 'Gender : %s; Weight : %dkg; Height : %dsm;\n' \
              ' Age : %d; Physical activity : %s; Calories : %f' % \
              ( gender, self.weight, self.height,
               self.age, view.str2[self.pa], self.calculate_calories())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
