from farm.domain.single_entities.chicken import Chicken
from farm.domain.single_entities.cow import Cow

class Builder:
    def __init__(self):
        self._species = None
        self._breed = None
        self._name = None
        self._age = None
        self._gender = None
        self._color = None
        self._feather_color = None
        self._number_of_horns = None

    def set_species(self, species):
        self._species = species
        return self

    def set_breed(self, breed):
        self._breed = breed
        return self

    def set_name(self, name):
        self._name = name
        return self

    def set_age(self, age):
        self._age = age
        return self

    def set_gender(self, gender):
        self._gender = gender
        return self

    def set_color(self, color):
        self._color = color
        return self
    
    def set_feather_color(self, feather_color):
        self._feather_color = feather_color
        return self

    def set_number_of_horns(self, number_of_horns):
        self._number_of_horns = number_of_horns
        return self

    def build(self):
        if self._species.lower() == "chicken":
            return Chicken(self._species, self._breed, self._name, self._age, self._gender, self._color, self._feather_color)
        elif self._species.lower() == "cow":
            return Cow(self._species, self._breed, self._name, self._age, self._gender, self._color, self._number_of_horns)
        else:
            raise ValueError(f"We don't allow {self._species} in this farm!")