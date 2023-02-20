import pytest
from typing import List

from farm.domain.collections.cow_pen import CowPen
from farm.domain.single_entities.cow import Cow
from farm.visitors.collections.add_visitor import AddVisitor
from farm.visitors.collections.get_animals_visitor import GetAnimalsVisitor
from farm.visitors.collections.get_animal_by_name_visitor import GetAnimalByNameVisitor

@pytest.fixture
def cow_pen():
    return CowPen()

@pytest.fixture
def cow():
    return Cow()

@pytest.fixture
def add_visitor():
    return AddVisitor()

@pytest.fixture
def get_animals_visitor():
    return GetAnimalsVisitor

@pytest.fixture
def get_animal_by_name_visitor():
    return GetAnimalByNameVisitor()

def test_can_instantiate(cow_pen):
    assert isinstance(cow_pen, CowPen)

def test_can_add(cow_pen, cow, add_visitor):
    cow_pen.capacity = 10
    cow_pen.accept(add_visitor, cow)
    assert len(cow_pen.cows) == 1

@pytest.mark.skip(reason="Works on main but not on test")
def test_can_get_animals(cow_pen, cow, add_visitor, get_animals_visitor):
    cow_pen.capacity = 10
    cow_pen.accept(add_visitor, cow)
    cows = cow_pen.accept(get_animals_visitor, "")
    assert isinstance(cows, List)

def test_can_get_animal_by_name(cow_pen, cow, add_visitor, get_animal_by_name_visitor):
    cow.name = "Bessie"
    cow_pen.capacity = 10
    cow_pen.accept(add_visitor, cow)
    cow_obj = cow_pen.accept(get_animal_by_name_visitor, "Bessie")
    assert cow_obj.name == "Bessie"
