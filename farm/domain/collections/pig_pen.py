from typing import List

from farm.domain.interfaces.habitat import Habitat
from farm.domain.single_entities.pig import Pig

class PigPen(Habitat):
    """
    PigPen Concrete Class

    Class that extends Habitat Abstract Class
    Supports Parallel class hierarchy

    Arguments:
        Habitat -- Habitat Base Class
    """
    def __init__(self) -> None:
        """
        __init__ method

        Attributes:
            pigs -- List[Pig]
        """
        self.pigs: List[Pig] = []

    # Liskov Substitution Principle
    def add(self, pig: Pig) -> None:
        """
        add method

        Method to add pig objects in pig_pen instance

        Arguments:
            pig -- Pig
        """
        self.pigs.append(pig)

    # Liskov Substitution Principle
    def get_animals(self) -> List[Pig]:
        """
        get_animals method

        Method to get all pig objects in pig_pen instnace

        Returns:
            self.pigs -- List[Pigs]
        """
        return self.pigs
