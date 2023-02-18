from typing import TypedDict, Any

from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder

class RequestParams(TypedDict):
    animal_builder: AbstractAnimalBuilder
    name: str
    species: str
    weight: int
    sound: str