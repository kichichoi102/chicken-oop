from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder
from farm.domain.collections.chicken_coop import ChickenCoop
from farm.domain.single_entities.chicken import Chicken

class ConcreteChickenCoopBuilder(AbstractHabitatBuilder):

    def __init__(self) -> None:
        self.chicken_coop: ChickenCoop = ChickenCoop()

    def build_capacity(self, capacity: int) -> None:
        self.chicken_coop.capacity = capacity

    def build_material(self, material: str) -> None:
        self.chicken_coop.material  = material

    def build_add_animal(self, chicken: Chicken) -> None:
        self.chicken_coop.add(chicken)

    def get_habitat(self) -> str:
        return f"""
        Chicken Coop:
        Capacity: {self.chicken_coop.capacity}
        Material: {self.chicken_coop.material}
        Number: {len(self.chicken_coop.chickens)}
        Animals: {[chicken.name for chicken in self.chicken_coop.chickens]}
        """