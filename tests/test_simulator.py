import pytest
from typing import Any
from src import Simulator


def test_instantiation_with_invalid_input():
    with pytest.raises(TypeError):
        Simulator(Any)
