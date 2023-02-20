from typing import Any
from typing_extensions import Unpack

from farm.builders.interfaces.request_params import RequestParams
from farm.domain.interfaces.animal import Animal
from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder

class AnimalHabitatDirector:
    """
    Director Class

    Director Class/Client interface to build habitat and 
    add respective animal to the habitat instance
    """

    def __init__(self, habitat_builder: AbstractHabitatBuilder) -> None:
        """
        __init__ method

        Animal Habitat Director Class init

        Arguments:
            builder -- AbstractHabitatBuilder
        """
        self.habitat_builder = habitat_builder

    def build_habitat(self, capacity: int, material: str) -> None:
        """
        build_habitat method

        setter/builder method to set attributes of 
        Habitat instance

        Arguments:
            capacity -- int
            material -- str
        """
        self.habitat_builder.build_capacity(capacity)
        self.habitat_builder.build_material(material)

    def add_animal(self, **kwargs: Unpack[RequestParams]) -> Animal:
        """
        add_animal method

        Method to create an instance of an animal with params
        outlined in RequestParams Type Interface
        """
        if "animal_builder" not in kwargs:
            raise TypeError('animal_builder parameter is required')
        animal_builder = kwargs['animal_builder']

        if "species" in kwargs:
            animal_builder.build_species(kwargs["species"])
        if "name" in kwargs:
            animal_builder.build_name(kwargs["name"])
        if "age" in kwargs:
            animal_builder.build_age(kwargs["age"])
        if "gender" in kwargs:
            animal_builder.build_gender(kwargs["gender"])
        if "color" in kwargs:
            animal_builder.build_color(kwargs["color"])
        if "weight" in kwargs:
            animal_builder.build_weight(kwargs["weight"])


        self.habitat_builder.build_add_animal(animal_builder.return_animal())

    def get_habitat(self) -> str:
        """
        get_habitat method

        method to get habitat details

        Returns:
            habitat detail string
        """
        return self.habitat_builder.get_habitat()
