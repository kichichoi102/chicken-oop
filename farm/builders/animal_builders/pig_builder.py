from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder
from farm.domain.single_entities.pig import Pig

class PigBuilder(AbstractAnimalBuilder):
    """
    PigBuilder Subclass

    Builder Class to set attributes to pig instance

    Arguments:
        AbstractAnimalBuilder -- AbstractAnimalBuilder
    """

    def __init__(self) -> None:
        """
        __init__ method

        Instantiates an instance of a pig
        """
        self.pig = Pig()

    def build_species(self, species:str="Pig") -> None:
        """
        build_species method

        setter/builder method to set species attribute 
        to Pig Instance

        Keyword Arguments:
            species -- str (default: {"Pig"})
        """
        self.pig.species = species

    def build_name(self, name:str="") -> None:
        """
        build_name method

        setter/builder method to set name attribute
        to Pig Instance

        Keyword Arguments:
            name -- str (default: {""})
        """
        self.pig.name = name

    def build_age(self, age:int=0) -> None:
        """
        build_age method

        setter/builder method to set age attribute
        to Pig Instance

        Keyword Arguments:
            age -- int (default: {0})
        """
        self.pig.age = age

    def build_gender(self, gender:str="") -> None:
        """
        build_gender method

        setter/builder method to set gender attribute
        to Pig Instance

        Keyword Arguments:
            gender -- str (default: {""})
        """
        self.pig.gender = gender
        
    def build_color(self, color:str="Pink") -> None:
        """
        build_color method

        setter/builder method to set color attribute
        to Pig Instance

        Keyword Arguments:
            color -- str (default: {"White"})
        """
        self.pig.color = color

    def build_weight(self, weight:int=1) -> None:
        """
        build_color method

        setter/builder method to set color attribute
        to Pig Instance

        Keyword Arguments:
            color -- str (default: {"White"})
        """
        self.pig.weight = weight

    def return_animal(self) -> Pig:
        return self.pig
