import pytest
from typing import Any
from src import Quadcopter


def test_instantiation_with_correct_model_name():
    Quadcopter('Tello', ip='192.168.10.1')


def test_instantiation_with_incorrect_model_name():
    with pytest.raises(NameError):
        Quadcopter('Name', ip='192.168.10.1')


def test_instantiation_with_invalid_input():
    with pytest.raises(TypeError):
        Quadcopter(Any, ip='192.168.10.1')


def test_unable_to_get_property_model():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with pytest.raises(PermissionError):
        print(drone.model)
