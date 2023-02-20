from typing import TypeVar

from farm.domain.interfaces.animal import Animal
from farm.visitors.interfaces.animal_visitor import AnimalVisitor

class Chicken(Animal):
    """
    Chicken Class

    Extends Abstract Animal Class

    Arguments:
        Animal -- Animal Super Class
    """
    def __init__(self) -> None:
        pass

    def accept(self, visitor:TypeVar('T', bound='AnimalVisitor')) -> None:
        """
        accept visitor interface method

        Takes in a visitor instance to run the incoming
        visitor methods

        Arguments:
            visitor -- Visitor
        """
        return visitor.visit_chicken(self)