from farm.domain.single_entities.chicken import Chicken

def test_can_instantiate():
    chicken = Chicken()
    assert isinstance(chicken, Chicken)

