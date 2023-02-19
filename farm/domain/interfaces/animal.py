from abc import ABC, abstractmethod

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
    def accept(self, visitor) -> None:
        """
        accept visitor interface abstract method

        Takes in a visitor instance to run the respective
        visitor methods

        Arguments:
            visitor -- Visitor
        """
        pass        
