from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder
from farm.domain.single_entities.cow import Cow


class CowBuilder(AbstractAnimalBuilder):
    """
    CowBuilder Subclass

    Builder Class to set attributes to cow instance

    Arguments:
        AbstractAnimalBuilder -- AbstractAnimalBuilder
    """

    def __init__(self) -> None:
        """
        __init__ method

        Instantiates an instance of a cow
        """
        self.cow: Cow = Cow()

    def build_species(self, species:str="Cow") -> None:
        """
        build_species method

        setter/builder method to set species attribute 
        to Cow Instance

        Keyword Arguments:
            species -- str (default: {"Cow"})
        """
        self.cow.species = species

    def build_name(self, name:str="") -> None:
        """
        build_name method

        setter/builder method to set name attribute
        to Cow Instance

        Keyword Arguments:
            name -- str (default: {""})
        """
        self.cow.name = name

    def build_age(self, age:int=0) -> None:
        """
        build_age method

        setter/builder method to set age attribute
        to Cow Instance

        Keyword Arguments:
            age -- int (default: {0})
        """
        self.cow.age = age

    def build_gender(self, gender:str="") -> None:
        """
        build_age method

        setter/builder method to set age attribute
        to Cow Instance

        Keyword Arguments:
            age -- int (default: {0})
        """
        self.cow.gender = gender
        
    def build_color(self, color:str="White") -> None:
        """
        build_color method

        setter/builder method to set color attribute
        to Cow Instance

        Keyword Arguments:
            color -- str (default: {"White"})
        """
        self.cow.color = color

    def build_weight(self, weight:int=1) -> None:
        """
        build_weight method

        setter/builder method to set weight attribute
        to Cow Instance

        Keyword Arguments:
            weight -- int (default: {1})
        """
        self.cow.weight = weight

    def return_animal(self) -> Cow:
        return self.cow
