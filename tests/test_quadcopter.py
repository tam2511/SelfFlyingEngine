import pytest
from src import Quadcopter


def test_instantiation_with_correct_model_name():
    Quadcopter('Tello', ip='192.168.10.1')


def test_instantiation_with_incorrect_model_name():
    with pytest.raises(NameError):
        Quadcopter('Name', ip='192.168.10.1')


def test_unable_to_get_property_model():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with pytest.raises(PermissionError):
        print(drone.model)
