from typing import List, Any, Optional, TypeVar
from abc import ABC, abstractmethod

from farm.domain.interfaces.animal import Animal
from farm.visitors.interfaces.habitat_visitor import HabitatVisitor

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
    def accept(self, visitor:TypeVar('T', bound='HabitatVisitor'), args:Any) -> Any:
        """
        accept visitor interface method

        Takes in a visitor instance to parse and run the incoming visitor methods

        Methods:
            add_visitor -- adds animal to respective habitat
            get_animals_visitor -- gets all respective animals in habitat
            get animal_by_name -- gets respective animal in habitat by name

        Arguments:
            args -- Chickens

        Keyword Arguments:
            visitor -- HabitatVisitor (default: {"HabitatVisitor")})

        Returns:
            Any
        """
        pass
