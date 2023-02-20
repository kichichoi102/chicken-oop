from farm.domain.single_entities.cow import Cow

def test_can_instantiate():
    cow = Cow()
    assert isinstance(cow, Cow)

