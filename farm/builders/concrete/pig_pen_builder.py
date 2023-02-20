from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder
from farm.domain.collections.pig_pen import PigPen
from farm.domain.single_entities.pig import Pig
from farm.visitors.collections.add_visitor import AddVisitor
from farm.visitors.collections.get_animals_visitor import GetAnimalsVisitor

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
        add_visitor = AddVisitor()
        self.pig_pen.accept(add_visitor, pig)

    def get_habitat(self) -> str:
        get_animals_builder = GetAnimalsVisitor()
        pigs_list = []
        if self.pig_pen.pigs[0] and self.pig_pen.pigs[0].name:
            pigs_list = [cow.name for cow in self.pig_pen.accept(get_animals_builder)]
        return f"""
        Pig Pen:
        Capacity: {self.pig_pen.capacity}
        Material: {self.pig_pen.material}
        Number: {len(self.pig_pen.accept(get_animals_builder))}
        Animals: {pigs_list}
        """