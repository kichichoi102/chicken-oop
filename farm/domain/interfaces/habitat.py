from typing import List
from abc import ABC, abstractmethod

from farm.domain.interfaces.animal import Animal

class Habitat(ABC):
    """
    Habitat Abstract Super Class

    Extends Abstract Base Class. Supports Parallel class hierarchy.
    Should not be instantiated

    Arguments:
        ABC -- Abstract Base Class
    """
    
    @abstractmethod
    def __init__(self, animal:Animal) -> None:
        pass

    @abstractmethod
    def add(self, animal:Animal) -> None:
        """
        add abstract method

        Method to add Base animal class to base habitat

        Arguments:
            animal -- _description_
        """
        pass

    @abstractmethod
    def get_animals(self) -> List[Animal]:
        """
        get_animals abstract method

        Abstract Method to get all base animals in base habitat instance

        Returns:
            List[Animals]
        """
        pass