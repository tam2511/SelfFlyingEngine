import pytest
from typing import Any
from src import Quadcopter, Session
from src.exceptions import UsageError


def test_instantiation_with_valid_input():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    Session(drone)


def test_instantiation_with_invalid_input():
    with pytest.raises(TypeError):
        Session(Any)


def test_unable_to_create_two_sessions_for_one_quadcopter():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    Session(drone)
    with pytest.raises(UsageError):
        Session(drone)


def test_property_quadcopter():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    session = Session(drone)
    assert type(session.quadcopter) is Quadcopter


def test_property_active():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    session = Session(drone)
    assert session.active is True

    session.finish()
    assert session.active is False


def test_one_session_cannot_finish_another_session():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    session1 = Session(drone)
    session1.finish()

    session2 = Session(drone)
    session1.finish()

    assert session2.active is True


def test_context_manager():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with Session(drone) as session:
        assert session.active is True

    assert session.active is False
