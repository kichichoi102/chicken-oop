import pytest
from farm.builders.interfaces.abstract_animal_builder import AbstractAnimalBuilder

def test_instantiate_abstract_raises_error():
    with pytest.raises(TypeError):
        AbstractAnimalBuilder()