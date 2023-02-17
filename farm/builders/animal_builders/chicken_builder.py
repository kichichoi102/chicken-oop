from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder
from farm.domain.single_entities.chicken import Chicken

class ChickenBuilder(AbstractAnimalBuilder):

    def __init__(self) -> None:
        self.chicken: Chicken = Chicken()

    def build_species(self, species:str="Chicken") -> None:
        self.chicken.species = species

    def build_name(self, name:str="") -> None:
        self.chicken.name = name

    def build_age(self, age:int=0) -> None:
        self.chicken.age = age

    def build_gender(self, gender:str="") -> None:
        self.chicken.gender = gender
        
    def build_color(self, color:str="White") -> None:
        self.chicken.color = color

    def build_weight(self, weight:int=1) -> None:
        self.chicken.weight = weight