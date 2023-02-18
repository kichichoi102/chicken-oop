from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder
from farm.domain.single_entities.pig import Pig

class PigBuilder(AbstractAnimalBuilder):

    def __init__(self) -> None:
        self.pig = Pig()

    def build_species(self, species:str="Pig") -> None:
        self.pig.species = species

    def build_name(self, name:str="") -> None:
        self.pig.name = name

    def build_age(self, age:int=0) -> None:
        self.pig.age = age

    def build_gender(self, gender:str="") -> None:
        self.pig.gender = gender
        
    def build_color(self, color:str="Pink") -> None:
        self.pig.color = color

    def build_weight(self, weight:int=1) -> None:
        self.pig.weight = weight

    def return_animal(self) -> Pig:
        return self.pig
