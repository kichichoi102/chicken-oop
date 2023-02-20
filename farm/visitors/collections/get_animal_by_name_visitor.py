from typing import Optional

from farm.visitors.interfaces.habitat_visitor import HabitatVisitor
from farm.exceptions.not_found_error import NotFoundError
from farm.domain.collections.chicken_coop import ChickenCoop
from farm.domain.collections.cow_pen import CowPen
from farm.domain.collections.pig_pen import PigPen
from farm.domain.single_entities.chicken import Chicken
from farm.domain.single_entities.cow import Cow
from farm.domain.single_entities.pig import Pig

class GetAnimalByNameVisitor(HabitatVisitor):
    """
    GetAnimalByNameVisitor Visitor Class

    Visitor methods to get animal by name in habitat

    Arguments:
        HabitatVisitor -- Abstract Visitor Interface

    Raises:
        NotFoundError -- name not found
    """

    EXCEPTIONSTRING = "Name not found"

    def visit_chicken_coop(self, chicken_coop: ChickenCoop, name:str) -> Optional[Chicken]:
        """
        visit_chicken_coop get_animal_by_name method

        Method to get chicken object in chicken_coop instance by name

        Arguments:
            chicken_coop -- chicken_coop object
            name -- query name

        Raises:
            NotFoundError -- name not found
        """
        for chicken in chicken_coop.chickens:
            if chicken.name == name:
                return chicken

        raise NotFoundError(GetAnimalByNameVisitor.EXCEPTIONSTRING)

    def visit_cow_pen(self, cow_pen:CowPen, name:str) -> Optional[Cow]:
        """
        visit_cow_pen get_animal_by_name method

        Method to get cow object in cow_pen instance by name

        Arguments:
            cow_pen -- cow_pen object
            name -- query name

        Raises:
            NotFoundError -- name not found
        """
        for cow in cow_pen.cows:
            if cow.name == name:
                return cow

        raise NotFoundError(GetAnimalByNameVisitor.EXCEPTIONSTRING)

    def visit_pig_pen(self, pig_pen:PigPen, name:str) -> Optional[Pig]:
        """
        visit_pig_pen get_animal_by_name method

        Method to get pig object in pig_pen instance by name

        Arguments:
            pig_pen -- pig_pen object
            name -- query name

        Raises:
            NotFoundError -- name not found
        """
        for pig in pig_pen.pigs:
            if pig.name == name:
                return pig

        raise NotFoundError(GetAnimalByNameVisitor.EXCEPTIONSTRING)
