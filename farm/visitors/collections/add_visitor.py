from farm.exceptions.capacity_full_error import CapacityFullError
from farm.visitors.interfaces.habitat_visitor import HabitatVisitor
from farm.domain.collections.chicken_coop import ChickenCoop
from farm.domain.collections.cow_pen import CowPen
from farm.domain.collections.pig_pen import PigPen
from farm.domain.single_entities.chicken import Chicken
from farm.domain.single_entities.cow import Cow
from farm.domain.single_entities.pig import Pig

class AddVisitor(HabitatVisitor):
    """
    AddVisitor Visitor Class

    Visitor methods to add animal to respective habitat

    Arguments:
        HabitatVisitor -- Abstract Visitor Interface

    Raises:
        CapacityFullError: Capacity is full
    """

    EXCEPTIONSTRING = "Capacity is full, cannot add more chickens"

    # Liskov Substitution Principle
    def visit_chicken_coop(self, chicken_coop:ChickenCoop, chicken:Chicken) -> None:
        """
        visit_chicken_coop Visitor Method

        Visitor method to add chicken to chicken_coop

        Arguments:
            chicken_coop -- chicken coop
            chicken -- chicken object

        Raises:
            CapacityFullError: capacity chicken_coop full
        """
        if len(chicken_coop.chickens) < chicken_coop.capacity:
            chicken_coop.chickens.append(chicken)
        else:
            raise CapacityFullError(AddVisitor.EXCEPTIONSTRING)

    # Liskov Substitution Principle
    def visit_cow_pen(self, cow_pen: CowPen, cow: Cow) -> None:
        """
        visit_cow_pen Visitor Method

        Visitor method to to add cows to cow_pen

        Arguments:
            cow_pen -- cow pen object
            cow -- cow object

        Raises:
            CapacityFullError: capacity of cow_pen is full
        """
        if len(cow_pen.cows) < cow_pen.capacity:
            cow_pen.cows.append(cow)
        else:
            raise CapacityFullError(AddVisitor.EXCEPTIONSTRING)

    # Liskov Substitution Principle
    def visit_pig_pen(self, pig_pen: PigPen, pig:Pig) -> None:
        """
        visit_pig_pen Visitor Method

        Visitor method to add pigs to pig_pen

        Arguments:
            pig_pen -- pig pen object
            pig -- pig object

        Raises:
            CapacityFullError: capacity of pig pen is full
        """
        if len(pig_pen.pigs) < pig_pen.capacity:
            pig_pen.pigs.append(pig)
        else:
            raise CapacityFullError(AddVisitor.EXCEPTIONSTRING)
