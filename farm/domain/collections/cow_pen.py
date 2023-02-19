from typing import List

from farm.domain.interfaces.habitat import Habitat
from farm.domain.single_entities.cow import Cow

class CowPen(Habitat):
    """
    CowPen Concrete Class

    Class that extends Habitat Abstract Class.
    Supports Parallel Class Hierarchy

    Arguments:
        Habitat -- Habitat Base Class
    """
    def __init__(self) -> None:
        """
        __init__ method

        Attributes:
            chickens -- List[Cow]
        """
        self.cows: List[Cow] = []

    # Liskov Substitution Principle
    def add(self, cow: Cow) -> None:
        """
        add method

        Method to add cow object to cow pen instance

        Arguments:
            cow -- Cow
        """
        self.cows.append(cow)

    # Liskov Substitution Principle
    def get_animals(self) -> List[Cow]:
        """
        get_animals method

        Metho to get all cow objects in cow_pen instance

        Returns:
            self.cows -- List[Cows]
        """
        return self.cows