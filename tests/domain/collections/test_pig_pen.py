import pytest
from typing import List

from farm.domain.collections.pig_pen import PigPen
from farm.domain.single_entities.pig import Pig

@pytest.fixture
def pig_pen():
    return PigPen()

@pytest.fixture
def pig():
    return Pig()

def test_can_instantiate(pig_pen):
    assert isinstance(pig_pen, PigPen)

def test_can_add(pig_pen, pig):
    pig_pen.add(pig)
    assert len(pig_pen.pigs) == 1

def test_can_get_animals(pig_pen, pig):
    pig_pen.add(pig)
    pigs = pig_pen.get_animals()
    assert isinstance(pigs, List)
