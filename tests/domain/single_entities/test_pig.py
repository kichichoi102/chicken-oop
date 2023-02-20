from farm.domain.single_entities.pig import Pig

def test_can_instantiate():
    pig = Pig()
    assert isinstance(pig, Pig)

