from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder
from farm.domain.collections.pig_pen import PigPen
from farm.domain.single_entities.pig import Pig

class ConcretePigPenBuilder(AbstractHabitatBuilder):
    """
    ConcretePigPenBuilder Subclass

    Concrete Builder Class to set attributes, add animal, and get details
    to a pig pen instance

    Arguments:
        AbstractHabitatBuilder -- AbstractHabitatBuilder
    """

    def __init__(self) -> None:
        """
        __init__ method

        Creates an instance of Pig pen
        """
        self.pig_pen: PigPen = PigPen()

    def build_capacity(self, capacity: int) -> None:
        """
        build_capacity method

        Setter/builder method to set capacity attribute
        of pig pen instance

        Arguments:
            capacity -- int
        """
        self.pig_pen.capacity = capacity

    def build_material(self, material: str) -> None:
        """
        build_material method

        Setter/builder method to set material attribute
        of pig pen instance

        Arguments:
            material -- str
        """
        self.pig_pen.material = material

    def build_add_animal(self, pig: Pig) -> None:
        """
        build_add_animal method

        Adds Pig instance to pig pen instance

        Arguments:
            pig -- Pig
        """
        self.pig_pen.add(pig)

    def get_habitat(self) -> str:
        return f"""
        Pig Pen:
        Capacity: {self.pig_pen.capacity}
        Material: {self.pig_pen.material}
        Number: {len(self.pig_pen.get_animals())}
        Animals: {[pig.name for pig in self.pig_pen.get_animals()]}
        """