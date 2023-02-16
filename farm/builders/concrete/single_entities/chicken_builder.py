from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder
from farm.domain.single_entities.chicken import Chicken

class ConcreteChickenBuilder(AbstractAnimalBuilder):

    def __init__(self):
        self.chicken = Chicken()

    def build_species(self, species:str="Chicken"):
        self.chicken.species = species

    def build_name(self, name:str=""):
        self.chicken.name = name

    def build_age(self, age:int=0):
        self.chicken.age = age

    def build_gender(self, gender:str=""):
        self._gender = gender
        
    def build_color(self, color:str="White"):
        self._color = None

    def build_weight(self, weight:int=1):
        self.chicken.weight = weight