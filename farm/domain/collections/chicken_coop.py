from typing import List, Any, TypeVar

from farm.domain.interfaces.habitat import Habitat
from farm.domain.single_entities.chicken import Chicken
from farm.visitors.interfaces.habitat_visitor import HabitatVisitor

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
        return visitor.visit_chicken_coop(self, args)
