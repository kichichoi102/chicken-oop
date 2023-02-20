import pytest

from farm.builders.animal_builders.chicken_builder import ChickenBuilder
from farm.domain.single_entities.chicken import Chicken

@pytest.fixture
def chicken_builder():
    return ChickenBuilder()

def test_can_instantiate_class(chicken_builder):
    assert isinstance(chicken_builder, ChickenBuilder)

def test_can_init_chicken(chicken_builder):
    assert isinstance(chicken_builder.chicken, Chicken)

def test_can_build_species(chicken_builder):
    chicken_builder.build_species("Chicken")
    assert chicken_builder.chicken.species == "Chicken"

def test_can_build_name(chicken_builder):
    chicken_builder.build_name("Name")
    assert chicken_builder.chicken.name == "Name"

def test_can_build_age(chicken_builder):
    chicken_builder.build_age(1)
    assert chicken_builder.chicken.age == 1

def test_can_build_gender(chicken_builder):
    chicken_builder.build_gender("Male")
    assert chicken_builder.chicken.gender == "Male"

def test_can_build_color(chicken_builder):
    chicken_builder.build_color("Red")
    assert chicken_builder.chicken.color == "Red"

def test_can_build_weight(chicken_builder):
    chicken_builder.build_weight(10)
    assert chicken_builder.chicken.weight == 10

def test_can_return_animal(chicken_builder):
    chicken = chicken_builder.return_animal()
    assert isinstance(chicken, Chicken)

