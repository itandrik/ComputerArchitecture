class Person:
    def __init__(self,first_name,
                 last_name,middle_name,
                 age,height,weight,
                 phone_number):
        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name
        self._age = age
        self._height = height
        self._weight = weight
        self._phone_number = phone_number


class Doctor:
    def __init__(self,first_name,
                 last_name,middle_name,
                 age,profession,
                 phone_number):
        self._first_name = first_name
        self._last_name = last_name
        self._middle_name = middle_name
        self._age = age
        self._profession = profession
        self._phone_number = phone_number