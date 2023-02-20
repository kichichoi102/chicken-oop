import pytest
from farm.domain.interfaces.habitat import Habitat

def test_instantiate_abstract_raises_error():
    with pytest.raises(TypeError):
        Habitat()