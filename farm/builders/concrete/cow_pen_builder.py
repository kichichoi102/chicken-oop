from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder
from farm.domain.collections.cow_pen import CowPen
from farm.domain.single_entities.cow import Cow

class ConcreteCowPenBuilder(AbstractHabitatBuilder):
    def __init__(self) -> None:
        self.cow_pen: CowPen = CowPen()

    def build_capacity(self, capacity: int):
        self.cow_pen.capacity = capacity

    def build_material(self, material: str):
        self.cow_pen.material = material

    def build_add_animal(self, cow: Cow):
        self.cow_pen.add(cow)

    def get_habitat(self) -> str:
        return f"""
        Cow Pen:
        Capacity: {self.cow_pen.capacity}
        Material: {self.cow_pen.material}
        Number: {len(self.cow_pen.get_animals())}
        Animals: {[cow.name for cow in self.cow_pen.get_animals()]}
        """