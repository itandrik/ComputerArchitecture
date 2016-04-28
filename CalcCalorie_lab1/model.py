import global_koefs
# Creating model. Describing functions,
# which calculate calories, using human parameters


class Model:
    def __init__(self, gender, weight, height, age, pa):
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age
        self.pa = pa

    def _calc(self, koefs):
        return koefs[0] + (koefs[1]*self.weight) + (koefs[2]*self.height) + (koefs[3]*self.age)

    # Calculating index of physical activity
    def _calculate_pa(self,pa):
        return global_koefs.activity_dict.get(pa, None)

    #Check if is male
    def is_male(self):
        return self.gender == 1

    # Calculating calories, which spend person per day
    def calculate_calories(self):
        # Calculating with Harris-Benedict formula
        hb_caloies = self._calc(global_koefs.coef['HB'][self.is_male()])

        # Calculating with Muffin-Jeor formula
        mj_calories = self._calc(global_koefs.coef['MJ'][self.is_male()])

        # Average value for more accuracy value
        return self._calculate_pa(self.pa) * ((hb_caloies + mj_calories) / 2)

    def get_info(self):
        gender = global_koefs.gender_coefs.get(self.is_male(), None)
        return ('Gender : %s; Weight : %dkg; Height : %dsm;\n'
               ' Age : %d; Physical activity : %s; Calories : %f') % \
              (gender, self.weight, self.height,
               self.age, global_koefs.str2[self.pa], self.calculate_calories())

