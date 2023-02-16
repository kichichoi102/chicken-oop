from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder
from farm.domain.collections.chicken_coop import ChickenCoop

class ConcreteChickenCoopBuilder(AbstractHabitatBuilder):

    def __init__(self):
        self.chicken_coop = ChickenCoop()

    def build_capacity(self, capacity):
        self.chicken_coop.capacity = capacity

    def build_material(self, material):
        self.chicken_coop.material = material

    def build_add_animal(self, chicken):
        self.chicken_coop.add(chicken)

    def get_habitat(self):
        return f"""
        Capacity: {self.chicken_coop.capacity}
        Material: {self.chicken_coop.material}
        Number: {len(self.chicken_coop.chickens)}
        Animals: {[chicken.name for chicken in self.chicken_coop.chickens]}
        """