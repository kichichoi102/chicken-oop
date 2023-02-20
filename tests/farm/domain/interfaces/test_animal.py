import pytest
from farm.domain.interfaces.animal import Animal

def test_instantiate_abstract_raises_error():
    with pytest.raises(TypeError):
        Animal()