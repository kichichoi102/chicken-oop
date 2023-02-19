from abc import ABC, abstractmethod

class AbstractAnimalBuilder(ABC):
    """
    AbstractAnimalBuilder Super Abstract Class

    Builder Interface that is extended for animal builders.
    Should not be instantiated.

    Arguments:
        ABC -- Abstract Base Class
    """

    @abstractmethod
    def __init__(self) -> None:
        """
        __init__ super abstract method

        Instantiates an instance of an animal
        """
        pass

    @abstractmethod
    def build_species(self, species:str) -> None:
        """
        build_species Super abstract  method

        setter/builder method to set species attribute
        to Animal

        Arguments:
            species -- str
        """
        pass

    @abstractmethod
    def build_name(self, name:str) -> None:
        """
        build_name Super abstract method

        setter/builder method to set name attribute
        to Animal

        Arguments:
            name -- str
        """
        pass

    @abstractmethod
    def build_age(self, age:int) -> None:
        """
        build_age Super abstract method

        setter/builder method to set age attribute
        to Animal

        Arguments:
            age -- int
        """
        pass

    @abstractmethod
    def build_gender(self, gender:str) -> None:
        """
        build_gender Super abstract method

        setter/builder method to set gender attribute
        to Animal

        Arguments:
            gender -- str
        """
        pass
        
    @abstractmethod
    def build_color(self, color:str) -> None:
        """
        build_color Super abstract method

        setter/builder method to set color attribute
        to Animal

        Arguments:
            color -- str
        """
        pass

    @abstractmethod
    def build_weight(self, weight:int) -> None:
        """
        build_weight Super abstract method

        setter/builder method to set weight attribute
        to Animal

        Arguments:
            weight -- str
        """
        pass

    @abstractmethod
    def return_animal(self) -> None:
        """
        return_animal Super abstract method

        setter/builder method to return Animal
        """
        pass
    