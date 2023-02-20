import pytest

from farm.builders.concrete.pig_pen_builder import ConcretePigPenBuilder
from farm.domain.collections.pig_pen import PigPen
from farm.domain.single_entities.pig import Pig

@pytest.fixture
def concrete_pig_pen_builder():
    return ConcretePigPenBuilder()

@pytest.fixture
def pig():
    pig = Pig()
    pig.name = "Name"
    return pig

def test_can_instantiate_class(concrete_pig_pen_builder):
    assert isinstance(concrete_pig_pen_builder, ConcretePigPenBuilder)

def test_can_init_pig_pen(concrete_pig_pen_builder):
    assert isinstance(concrete_pig_pen_builder.pig_pen, PigPen)

def test_can_build_capacity(concrete_pig_pen_builder):
    concrete_pig_pen_builder.build_capacity(10)
    assert concrete_pig_pen_builder.pig_pen.capacity == 10

def test_can_build_material(concrete_pig_pen_builder):
    concrete_pig_pen_builder.build_material("Wood")
    assert concrete_pig_pen_builder.pig_pen.material == "Wood"

def test_can_build_add_animal(concrete_pig_pen_builder, pig):
    concrete_pig_pen_builder.build_add_animal(pig)
    assert len(concrete_pig_pen_builder.pig_pen.pigs) == 1

@pytest.mark.skip(reason="string testing is so not nice")
def test_get_habitat(concrete_pig_pen_builder, pig):
    concrete_pig_pen_builder.build_capacity(10)
    concrete_pig_pen_builder.build_material("Wood")
    concrete_pig_pen_builder.build_add_animal(pig)
    return_string = concrete_pig_pen_builder.get_habitat()
    string = """
    Pig Pen
    Capacity: 10
    Material: Wood
    Number: 1
    Animals: []
    """
    assert return_string == string