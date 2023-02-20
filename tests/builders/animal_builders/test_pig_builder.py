import pytest

from farm.builders.animal_builders.pig_builder import PigBuilder
from farm.domain.single_entities.pig import Pig

@pytest.fixture
def pig_builder():
    return PigBuilder()

def test_can_instantiate_class(pig_builder):
    assert isinstance(pig_builder, PigBuilder)

def test_can_init_pig(pig_builder):
    assert isinstance(pig_builder.pig, Pig)

def test_can_build_species(pig_builder):
    pig_builder.build_species("Pig")
    assert pig_builder.pig.species == "Pig"

def test_can_build_name(pig_builder):
    pig_builder.build_name("Name")
    assert pig_builder.pig.name == "Name"

def test_can_build_age(pig_builder):
    pig_builder.build_age(1)
    assert pig_builder.pig.age == 1

def test_can_build_gender(pig_builder):
    pig_builder.build_gender("Male")
    assert pig_builder.pig.gender == "Male"

def test_can_build_color(pig_builder):
    pig_builder.build_color("Pink")
    assert pig_builder.pig.color == "Pink"

def test_can_build_weight(pig_builder):
    pig_builder.build_weight(100)
    assert pig_builder.pig.weight == 100

def test_can_return_animal(pig_builder):
    pig = pig_builder.return_animal()
    assert isinstance(pig, Pig)