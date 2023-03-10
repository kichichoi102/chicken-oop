from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder
from farm.domain.collections.chicken_coop import ChickenCoop
from farm.domain.single_entities.chicken import Chicken
from farm.visitors.collections.add_visitor import AddVisitor
from farm.visitors.collections.get_animals_visitor import GetAnimalsVisitor

class ConcreteChickenCoopBuilder(AbstractHabitatBuilder):
    """
    ConcreteChickenCoopBuilder Subclass

    Concrete Builder Class to set attributes, add animal, and get details
    to a chicken coop instance

    Arguments:
        AbstractHabitatBuilder -- AbstractHabitatBuilder
    """

    def __init__(self) -> None:
        """
        __init__ method

        Creates an instance of Chicken Coop
        """
        self.chicken_coop: ChickenCoop = ChickenCoop()

    def build_capacity(self, capacity: int) -> None:
        """
        build_capacity method

        Setter/builder method to set capacity attribute
        of chicken coop instance

        Arguments:
            capacity -- int
        """
        self.chicken_coop.capacity = capacity

    def build_material(self, material: str) -> None:
        """
        build_material method

        Setter/builder method to set material attribute
        of chicken coop instance

        Arguments:
            material -- str
        """
        self.chicken_coop.material  = material

    def build_add_animal(self, chicken: Chicken) -> None:
        """
        build_add_animal method

        Adds Chicken instance to chicken coop instance

        Arguments:
            chicken -- Chicken
        """
        add_visitor = AddVisitor()
        self.chicken_coop.accept(add_visitor, chicken)

    def get_habitat(self) -> str:
        get_animals_visitor = GetAnimalsVisitor()
        chicken_list = []
        if self.chicken_coop.chickens[0] and self.chicken_coop.chickens[0].name:
            chicken_list = [chicken.name for chicken in \
            self.chicken_coop.accept(get_animals_visitor)]
        return f"""
        Chicken Coop:
        Capacity: {self.chicken_coop.capacity}
        Material: {self.chicken_coop.material}
        Number: {len(self.chicken_coop.accept(get_animals_visitor))}
        Animals: {chicken_list}
        """