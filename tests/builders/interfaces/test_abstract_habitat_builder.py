import pytest
from farm.builders.interfaces.abstract_habitat_builder import AbstractHabitatBuilder

def test_instantiate_abstract_raises_error():
    with pytest.raises(TypeError):
        AbstractHabitatBuilder()