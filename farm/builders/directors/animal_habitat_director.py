from typing import Any
from typing_extensions import Unpack

from farm.builders.interfaces.request_params import RequestParams
from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder
from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder

class AnimalHabitatDirector:
    """
    Director Class

    Director Class/Client interface to build habitat and 
    add respective animal to the habitat instance
    """

    def __init__(self, builder: AbstractHabitatBuilder) -> None:
        """
        __init__ method

        Animal Habitat Director Class init

        Arguments:
            builder -- AbstractHabitatBuilder
        """
        self.builder = builder

    def build_habitat(self, capacity: int, material: str) -> None:
        """
        build_habitat method

        setter/builder method to set attributes of 
        Habitat instance

        Arguments:
            capacity -- int
            material -- str
        """
        self.builder.build_capacity(capacity)
        self.builder.build_material(material)

    def add_animal(self, **kwargs: Unpack[RequestParams]) -> None:
        """
        add_animal method

        Method to create an instance of an animal with params
        outlined in RequestParams Type Interface
        """
        animal_builder = kwargs['animal_builder']
        animal_builder.build_species(kwargs["species"])
        animal_builder.build_name(kwargs["name"])
        animal_builder.build_weight(kwargs["weight"])


        self.builder.build_add_animal(animal_builder.return_animal())

    def get_habitat(self) -> Any:
        """
        get_habitat method

        method to get habitat details

        Returns:
            habitat detail string
        """
        return self.builder.get_habitat()