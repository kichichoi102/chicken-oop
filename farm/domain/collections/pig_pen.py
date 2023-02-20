from typing import List, Any, TypeVar

from farm.domain.interfaces.habitat import Habitat
from farm.domain.single_entities.pig import Pig
from farm.visitors.interfaces.habitat_visitor import HabitatVisitor

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

    def accept(self, visitor:TypeVar('T', bound='HabitatVisitor'), args:Any="") -> Any:
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
        return visitor.visit_pig_pen(self, args)

