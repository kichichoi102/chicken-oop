from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder
from farm.domain.single_entities.chicken import Chicken

class ChickenBuilder(AbstractAnimalBuilder):
    """
    ChickenBuilder Subclass

    Builder Class to set attributes to chicken instance

    Arguments:
        AbstractAnimalBuilder -- AbstractAnimalBuilder
    """

    def __init__(self) -> None:
        """
        __init__ method

        Instantiates an instance of a chicken
        """
        self.chicken: Chicken = Chicken()

    def build_species(self, species:str="Chicken") -> None:
        """
        build_species method

        setter/builder method to set species attribute 
        to Chicken Instance

        Keyword Arguments:
            species -- str (default: {"Chicken"})
        """
        self.chicken.species = species

    def build_name(self, name:str="") -> None:
        """
        build_name method

        setter/builder method to set name attribute
        to Chicken Instance

        Keyword Arguments:
            name -- str (default: {""})
        """
        self.chicken.name = name

    def build_age(self, age:int=0) -> None:
        """
        build_age method

        setter/builder method to set age attribute
        to Chicken Instance

        Keyword Arguments:
            age -- int (default: {0})
        """
        self.chicken.age = age

    def build_gender(self, gender:str="") -> None:
        """
        build_gender method

        setter/builder method to set gender attribute
        to Chicken Instance

        Keyword Arguments:
            gender -- str (default: {""})
        """
        self.chicken.gender = gender
        
    def build_color(self, color:str="White") -> None:
        """
        build_color method

        setter/builder method to set color attribute
        to Chicken Instance

        Keyword Arguments:
            color -- str (default: {"White"})
        """
        self.chicken.color = color

    def build_weight(self, weight:int=1) -> None:
        """
        build_color method

        setter/builder method to set color attribute
        to Chicken Instance

        Keyword Arguments:
            color -- str (default: {"White"})
        """
        self.chicken.weight = weight

    def return_animal(self) -> Chicken:
        return self.chicken