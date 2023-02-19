from abc import ABC, abstractmethod
from farm.domain.interfaces.animal import Animal

class AbstractHabitatBuilder(ABC):
    """
    AbstractHabitatBuilder Super Abstract Class

    Builder Interface that is extended for animal habitat builders.
    Should not be instantiated.

    Arguments:
        ABC -- Abstract Base Class
    """
    
    @abstractmethod
    def build_capacity(self, capacity: int) -> None:
        """
        build_capacity super abstract method

        setter/builder method to set capacity attribute
        to Habitat

        Arguments:
            capacity -- int
        """
        pass

    @abstractmethod
    def build_material(self, material: str) -> None:
        """
        build_material super abstract method

        setter/builder method to set material attribute
        to Habitat

        Arguments:
            material -- str
        """
        pass

    @abstractmethod
    def build_add_animal(self, animal: Animal) -> None:
        """
        build_add_animal super abstract method

        Abstract method to add animal to habitat

        Arguments:
            animal -- Animal
        """
        pass

    @abstractmethod
    def get_habitat(self) -> None:
        """
        get_habitat abstract method

        Abstract method to return details of habitat
        """
        pass