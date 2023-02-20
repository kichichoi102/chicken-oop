import pytest

from farm.builders.concrete.cow_pen_builder import ConcreteCowPenBuilder
from farm.domain.collections.cow_pen import CowPen
from farm.domain.single_entities.cow import Cow

@pytest.fixture
def concrete_cow_pen_builder():
    return ConcreteCowPenBuilder()

@pytest.fixture
def cow():
    cow = Cow()
    cow.name = "Name"
    return cow

def test_can_instantiate_class(concrete_cow_pen_builder):
    assert isinstance(concrete_cow_pen_builder, ConcreteCowPenBuilder)

def test_can_init_cow_pen(concrete_cow_pen_builder):
    assert isinstance(concrete_cow_pen_builder.cow_pen, CowPen)

def test_can_build_capacity(concrete_cow_pen_builder):
    concrete_cow_pen_builder.build_capacity(10)
    assert concrete_cow_pen_builder.cow_pen.capacity == 10

def test_can_build_material(concrete_cow_pen_builder):
    concrete_cow_pen_builder.build_material("Wood")
    assert concrete_cow_pen_builder.cow_pen.material == "Wood"

def test_can_build_add_animal(concrete_cow_pen_builder, cow):
    concrete_cow_pen_builder.build_capacity(10)
    concrete_cow_pen_builder.build_add_animal(cow)
    assert len(concrete_cow_pen_builder.cow_pen.cows) == 1

@pytest.mark.skip(reason="string testing is so not nice")
def test_get_habitat(concrete_cow_pen_builder, cow):
    concrete_cow_pen_builder.build_capacity(10)
    concrete_cow_pen_builder.build_material("Wood")
    concrete_cow_pen_builder.build_add_animal(cow)
    return_string = concrete_cow_pen_builder.get_habitat()
    string = """
    Cow Pen
    Capacity: 10
    Material: Wood
    Number: 1
    Animals: []
    """
    assert return_string == string