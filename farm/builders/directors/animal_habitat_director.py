from typing import Any
from typing_extensions import Unpack

from farm.builders.directors.request_params import RequestParams
from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder
from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder

class AnimalHabitatDirector:

    def __init__(self, builder: AbstractHabitatBuilder) -> None:
        self.builder = builder

    def build_habitat(self, capacity: int, material: str) -> None:
        self.builder.build_capacity(capacity)
        self.builder.build_material(material)

    def add_animal(self, **kwargs: Unpack[RequestParams]) -> None:
        animal_builder = kwargs['animal_builder']
        animal_builder.build_species(kwargs["species"])
        animal_builder.build_name(kwargs["name"])
        animal_builder.build_weight(kwargs["weight"])

        self.builder.build_add_animal(animal_builder.chicken)

    def get_habitat(self) -> Any:
        return self.builder.get_habitat()