import pytest
from typing import List

from farm.domain.collections.pig_pen import PigPen
from farm.domain.single_entities.pig import Pig
from farm.visitors.collections.add_visitor import AddVisitor
from farm.visitors.collections.get_animals_visitor import GetAnimalsVisitor
from farm.visitors.collections.get_animal_by_name_visitor import GetAnimalByNameVisitor

@pytest.fixture
def pig_pen():
    return PigPen()

@pytest.fixture
def pig():
    return Pig()

@pytest.fixture
def add_visitor():
    return AddVisitor()

@pytest.fixture
def get_animals_visitor():
    return GetAnimalsVisitor()

@pytest.fixture
def get_animal_by_name_visitor():
    return GetAnimalByNameVisitor()

def test_can_instantiate(pig_pen):
    assert isinstance(pig_pen, PigPen)

def test_can_add(pig_pen, pig, add_visitor):
    pig_pen.capacity = 10
    pig_pen.accept(add_visitor, pig)
    assert len(pig_pen.pigs) == 1

def test_can_get_animals(pig_pen, pig, add_visitor, get_animals_visitor):
    pig_pen.capacity = 10
    pig_pen.accept(add_visitor, pig)
    pigs = pig_pen.accept(get_animals_visitor, "")
    assert isinstance(pigs, List)

def test_can_get_animal_by_name(pig_pen, pig, add_visitor, get_animal_by_name_visitor):
    pig.name = "Mimi"
    pig_pen.capacity = 10
    pig_pen.accept(add_visitor, pig)
    pig_obj = pig_pen.accept(get_animal_by_name_visitor, "Mimi")
    assert pig_obj.name == "Mimi"
