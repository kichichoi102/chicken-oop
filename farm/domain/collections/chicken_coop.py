from typing import List

from farm.domain.interfaces.habitat import Habitat
from farm.domain.single_entities.chicken import Chicken
from farm.domain.interfaces.animal import Animal

class ChickenCoop(Habitat):
    """
    ChickenCoop Concrete Class

    Class that extends Habitat Abstract Class. 
    Supports Parallel class hierarchy

    Arguments:
        Habitat -- Habitat Base Class
    """
    def __init__(self) -> None:
        """
        __init__ method

        Attributes:
            chickens -- List[Chicken]
        """
        self.chickens: List[Chicken] = []

    # Liskov Substitution Principle
    # talking point hehe
    def add(self, chicken: Chicken) -> None:
        """
        add method

        Method to add chicken object to chicken coop

        Arguments:
            chicken -- Chicken
        """
        self.chickens.append(chicken)

    # Liskov Substitution Principle
    def get_animals(self) -> List[Chicken]:
        """
        get_animals method

        Method to get all chicken objects in chicken_coop instance

        Returns:
            self.chickens -- List[Chickens]
        """
        return self.chickens