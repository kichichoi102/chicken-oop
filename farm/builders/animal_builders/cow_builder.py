from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder
from farm.domain.single_entities.cow import Cow


class CowBuilder(AbstractAnimalBuilder):

    def __init__(self) -> None:
        self.cow: Cow = Cow()

    def build_species(self, species:str="Cow") -> None:
        self.cow.species = species

    def build_name(self, name:str="") -> None:
        self.cow.name = name

    def build_age(self, age:int=0) -> None:
        self.cow.age = age

    def build_gender(self, gender:str="") -> None:
        self.cow.gender = gender
        
    def build_color(self, color:str="White") -> None:
        self.cow.color = color

    def build_weight(self, weight:int=1) -> None:
        self.cow.weight = weight

    def return_animal(self) -> Cow:
        return self.cow
