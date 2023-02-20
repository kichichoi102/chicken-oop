import pytest
from typing import List

from farm.domain.collections.chicken_coop import ChickenCoop
from farm.domain.single_entities.chicken import Chicken
from farm.visitors.collections.add_visitor import AddVisitor
from farm.visitors.collections.get_animals_visitor import GetAnimalsVisitor
from farm.visitors.collections.get_animal_by_name_visitor import GetAnimalByNameVisitor

@pytest.fixture
def chicken_coop():
    return ChickenCoop()

@pytest.fixture
def chicken():
    return Chicken()

@pytest.fixture
def add_visitor():
    return AddVisitor()

@pytest.fixture
def get_animals_visitor():
    return GetAnimalsVisitor()

@pytest.fixture
def get_animal_by_name_visitor():
    return GetAnimalByNameVisitor()

def test_can_instantiate(chicken_coop):
    assert isinstance(chicken_coop, ChickenCoop)

def test_can_add(chicken_coop, chicken, add_visitor):
    chicken_coop.capacity = 10
    chicken_coop.accept(add_visitor, chicken)
    assert len(chicken_coop.chickens) == 1

def test_can_get_animals(chicken_coop, chicken, add_visitor, get_animals_visitor):
    chicken_coop.capacity = 10
    chicken_coop.accept(add_visitor, chicken)
    chickens = chicken_coop.accept(get_animals_visitor, "")

    assert isinstance(chickens, List)

def test_can_get_animal_by_name(chicken_coop, chicken, add_visitor, get_animal_by_name_visitor):
    chicken.name = "Henrietta"
    chicken_coop.capacity = 10
    chicken_coop.accept(add_visitor, chicken)
    chicken_obj = chicken_coop.accept(get_animal_by_name_visitor, "Henrietta")
    assert chicken_obj.name == "Henrietta"
