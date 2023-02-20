import pytest
from typing import List

from farm.domain.collections.chicken_coop import ChickenCoop
from farm.domain.single_entities.chicken import Chicken

@pytest.fixture
def chicken_coop():
    return ChickenCoop()

@pytest.fixture
def chicken():
    return Chicken()

def test_can_instantiate(chicken_coop):
    assert isinstance(chicken_coop, ChickenCoop)

def test_can_add(chicken_coop, chicken):
    chicken_coop.add(chicken)
    assert len(chicken_coop.chickens) == 1

def test_can_get_animals(chicken_coop, chicken):
    chicken_coop.add(chicken)
    chickens = chicken_coop.get_animals()
    assert isinstance(chickens, List)

def test_can_get_animal_by_name(chicken_coop, chicken):
    chicken.name = "Henrietta"
    chicken_coop.add(chicken)
    chicken_obj = chicken_coop.get_animal_by_name("Henrietta")
    assert chicken_obj.name == "Henrietta"
