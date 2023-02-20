from typing import TypedDict, Any

from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder

class RequestParams(TypedDict):
    animal_builder: AbstractAnimalBuilder
    species:str
    name: str
    age: int
    gender: str
    color: str
    weight: int