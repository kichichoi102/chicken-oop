import pytest

from farm.builders.directors.animal_habitat_director import AnimalHabitatDirector
from farm.builders.concrete.chicken_coop_builder import ConcreteChickenCoopBuilder
from farm.builders.animal_builders.chicken_builder import ChickenBuilder

@pytest.fixture
def chicken_builder():
    return ChickenBuilder()

@pytest.fixture
def concrete_chicken_coop_builder():
    return ConcreteChickenCoopBuilder()

@pytest.fixture
def animal_habitat_director(concrete_chicken_coop_builder):
    return AnimalHabitatDirector(concrete_chicken_coop_builder)

def test_can_instantiate_class(animal_habitat_director):
    assert isinstance(animal_habitat_director, AnimalHabitatDirector)

def test_can_init(animal_habitat_director):
    assert isinstance(animal_habitat_director.habitat_builder, ConcreteChickenCoopBuilder)

def test_can_build_habitat(animal_habitat_director):
    animal_habitat_director.build_habitat(10, "Wood")
    assert (animal_habitat_director.habitat_builder.chicken_coop.capacity == 10) \
        and (animal_habitat_director.habitat_builder.chicken_coop.material == "Wood")

def test_can_add_animal(animal_habitat_director, concrete_chicken_coop_builder, chicken_builder):
    concrete_chicken_coop_builder.build_capacity(10)
    animal_habitat_director.add_animal(
        animal_builder = chicken_builder,
        species = "Chicken",
        name = "Name",
        age=1,
        gender="Male",
        color="White",
        weight = 10
    )
    chicken = animal_habitat_director.habitat_builder.chicken_coop.chickens[0]
    assert chicken.species == "Chicken" and \
        chicken.name == "Name" and \
        chicken.age==1 and \
        chicken.gender=="Male" and \
        chicken.color=="White" and \
        chicken.weight == 10

