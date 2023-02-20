from typing import List

from farm.visitors.interfaces.habitat_visitor import HabitatVisitor
from farm.domain.collections.chicken_coop import ChickenCoop
from farm.domain.collections.cow_pen import CowPen
from farm.domain.collections.pig_pen import PigPen
from farm.domain.single_entities.chicken import Chicken
from farm.domain.single_entities.cow import Cow
from farm.domain.single_entities.pig import Pig

class GetAnimalsVisitor(HabitatVisitor):
    """
    GetAnimalsVisitor Visitor Class

    Visitor methods to get all animals in habitat

    Arguments:
        HabitatVisitor -- Abstract Visitor Interface
    """

    # Liskov Substitution Principle
    def visit_chicken_coop(self, chicken_coop: ChickenCoop, args) -> List[Chicken]:
        """
        visit_chicken_coop get_animals method

        Method to get all chicken objects in chicken_coop

        Arguments:
            chicken_coop -- chicken_coop object

        Returns:
            List[Chicken]
        """
        return chicken_coop.chickens

    # Liskov Substitution Principle
    def visit_cow_pen(self, cow_pen: CowPen, args) -> List[Cow]:
        """
        visit_cow_pen get_animals method

        Method to get all cow objects in cow_pen

        Arguments:
            cow_pen -- cow_pen object

        Returns:
            List[Cow]
        """
        return cow_pen.cows

    # Liskov Substitution Principle
    def visit_pig_pen(self, pig_pen:PigPen, args) -> List[Pig]:
        """
        visit_pig_pen get_animals method

        Methods to get all pig objects in pig_pen

        Arguments:
            pig_pen -- pig_pen object

        Returns:
            List[Pig]
        """
        return pig_pen.pigs