import pytest

from farm.builders.animal_builders.cow_builder import CowBuilder
from farm.domain.single_entities.cow import Cow

@pytest.fixture
def cow_builder():
    return CowBuilder()

def test_can_instantiate_class(cow_builder):
    assert isinstance(cow_builder, CowBuilder)

def test_can_init_cow(cow_builder):
    assert isinstance(cow_builder.cow, Cow)

def test_can_build_species(cow_builder):
    cow_builder.build_species("Cow")
    assert cow_builder.cow.species == "Cow"

def test_can_build_name(cow_builder):
    cow_builder.build_name("Name")
    assert cow_builder.cow.name == "Name"

def test_can_build_age(cow_builder):
    cow_builder.build_age(1)
    assert cow_builder.cow.age == 1

def test_can_build_gender(cow_builder):
    cow_builder.build_gender("Male")
    assert cow_builder.cow.gender == "Male"

def test_can_build_color(cow_builder):
    cow_builder.build_color("White")
    assert cow_builder.cow.color == "White"

def test_can_build_weight(cow_builder):
    cow_builder.build_weight(100)
    assert cow_builder.cow.weight == 100

def test_can_return_animal(cow_builder):
    cow = cow_builder.return_animal()
    assert isinstance(cow, Cow)