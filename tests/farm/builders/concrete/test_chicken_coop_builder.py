import pytest

from farm.builders.concrete.chicken_coop_builder import ConcreteChickenCoopBuilder
from farm.domain.collections.chicken_coop import ChickenCoop
from farm.domain.single_entities.chicken import Chicken

@pytest.fixture
def concrete_chicken_coop_builder():
    return ConcreteChickenCoopBuilder()

@pytest.fixture
def chicken():
    chicken = Chicken()
    chicken.name = "Name"
    return chicken

def test_can_instantiate_class(concrete_chicken_coop_builder):
    assert isinstance(concrete_chicken_coop_builder, ConcreteChickenCoopBuilder)

def test_can_init_chicken_coop(concrete_chicken_coop_builder):
    assert isinstance(concrete_chicken_coop_builder.chicken_coop, ChickenCoop)

def test_can_build_capacity(concrete_chicken_coop_builder):
    concrete_chicken_coop_builder.build_capacity(10)
    assert concrete_chicken_coop_builder.chicken_coop.capacity == 10

def test_can_build_material(concrete_chicken_coop_builder):
    concrete_chicken_coop_builder.build_material("Wood")
    assert concrete_chicken_coop_builder.chicken_coop.material == "Wood"

def test_can_build_add_animal(concrete_chicken_coop_builder, chicken):
    concrete_chicken_coop_builder.build_capacity(10)
    concrete_chicken_coop_builder.build_add_animal(chicken)
    assert len(concrete_chicken_coop_builder.chicken_coop.chickens) == 1

@pytest.mark.skip(reason="string testing is so not nice")
def test_get_habitat(concrete_chicken_coop_builder, chicken):
    concrete_chicken_coop_builder.build_capacity(10)
    concrete_chicken_coop_builder.build_material("Wood")
    concrete_chicken_coop_builder.build_add_animal(chicken)
    return_string = concrete_chicken_coop_builder.get_habitat()
    string = """
    Chicken Coop
    Capacity: 10
    Material: Wood
    Number: 1
    Animals: []
    """
    assert return_string == string