from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder
from farm.domain.collections.pig_pen import PigPen
from farm.domain.single_entities.pig import Pig

class ConcretePigPenBuilder(AbstractHabitatBuilder):

    def __init__(self) -> None:
        self.pig_pen: PigPen = PigPen()

    def build_capacity(self, capacity: int) -> None:
        self.pig_pen.capacity = capacity

    def build_material(self, material: str) -> None:
        self.pig_pen.material = material

    def build_add_animal(self, pig: Pig) -> None:
        self.pig_pen.add(pig)

    def get_habitat(self) -> str:
        return f"""
        Pig Pen:
        Capacity: {self.pig_pen.capacity}
        Material: {self.pig_pen.material}
        Number: {len(self.pig_pen.get_animals())}
        Animals: {[pig.name for pig in self.pig_pen.get_animals()]}
        """