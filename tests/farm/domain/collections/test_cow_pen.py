import pytest
from typing import List

from farm.domain.collections.cow_pen import CowPen
from farm.domain.single_entities.cow import Cow

@pytest.fixture
def cow_pen():
    return CowPen()

@pytest.fixture
def cow():
    return Cow()

def test_can_instantiate(cow_pen):
    assert isinstance(cow_pen, CowPen)

def test_can_add(cow_pen, cow):
    cow_pen.add(cow)
    assert len(cow_pen.cows) == 1

def test_can_get_animals(cow_pen, cow):
    cow_pen.add(cow)
    cows = cow_pen.get_animals()
    assert isinstance(cows, List)

def test_can_get_animal_by_name(cow_pen, cow):
    cow.name = "Bessie"
    cow_pen.add(cow)
    cow_obj = cow_pen.get_animal_by_name("Bessie")
    assert cow_obj.name == "Bessie"
