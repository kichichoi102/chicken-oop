from abc import ABC, abstractmethod
from typing import TypeVar

from farm.visitors.interfaces.animal_visitor import AnimalVisitor

class Animal(ABC):
    """
    Animal Abstract Super Class

    Extends Abstract Base class.
    Should not be instantiated.

    Arguments:
        ABC -- Abstract Base Class
    """

    @abstractmethod
    def __init__(self)  -> None:
        pass

    @abstractmethod
    def accept(self, visitor:TypeVar("T", bound="AnimalVisitor")) -> None:
        """
        accept visitor interface abstract method

        Takes in a visitor instance to run the respective
        visitor methods

        Arguments:
            visitor -- Visitor
        """
        pass
