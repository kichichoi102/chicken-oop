from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder
from farm.domain.collections.cow_pen import CowPen
from farm.domain.single_entities.cow import Cow
from farm.visitors.collections.add_visitor import AddVisitor
from farm.visitors.collections.get_animals_visitor import GetAnimalsVisitor

class ConcreteCowPenBuilder(AbstractHabitatBuilder):
    """
    ConcreteCowPenBuilder Subclass

    Concrete Builder Class to set attributes, add animal, and get details
    to a cow pen instance

    Arguments:
        AbstractHabitatBuilder -- AbstractHabitatBuilder
    """

    def __init__(self) -> None:
        """
        __init__ method

        Creates an instance of Cow Pen
        """
        self.cow_pen: CowPen = CowPen()

    def build_capacity(self, capacity: int):
        """
        build_capacity method

        Setter/builder method to set capacity attribute
        of cow pen instance

        Arguments:
            capacity -- int
        """
        self.cow_pen.capacity = capacity

    def build_material(self, material: str):
        """
        build_material method

        Setter/builder method to set material attribute
        of cow pen instance

        Arguments:
            material -- str
        """
        self.cow_pen.material = material

    def build_add_animal(self, cow: Cow):
        """
        build_add_animal method

        Adds Cow instance to cow pen instance

        Arguments:
            cow -- Cow
        """
        add_visitor = AddVisitor()
        self.cow_pen.accept(add_visitor, cow)

    def get_habitat(self) -> str:
        get_animals_builder = GetAnimalsVisitor()
        cows_list = []
        if self.cow_pen.cows[0] and self.cow_pen.cows[0].name:
            cows_list = [cow.name for cow in self.cow_pen.accept(get_animals_builder)]
        return f"""
        Cow Pen:
        Capacity: {self.cow_pen.capacity}
        Material: {self.cow_pen.material}
        Number: {len(self.cow_pen.accept(get_animals_builder))}
        Animals: {cows_list}
        """