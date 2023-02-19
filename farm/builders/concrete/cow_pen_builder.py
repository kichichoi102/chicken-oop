from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder
from farm.domain.collections.cow_pen import CowPen
from farm.domain.single_entities.cow import Cow

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
        self.cow_pen.add(cow)

    def get_habitat(self) -> str:
        return f"""
        Cow Pen:
        Capacity: {self.cow_pen.capacity}
        Material: {self.cow_pen.material}
        Number: {len(self.cow_pen.get_animals())}
        Animals: {[cow.name for cow in self.cow_pen.get_animals()]}
        """