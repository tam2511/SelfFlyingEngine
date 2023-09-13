import pytest
from typing import Any
from src import Quadcopter, Session, Control
from src.exceptions import UsageError


def test_instantiation_with_valid_input():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    session = Session(drone)
    Control(session)


def test_instantiation_with_invalid_input():
    with pytest.raises(TypeError):
        Control(Any)


def test_unable_to_create_two_controls_for_one_session():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    session = Session(drone)
    Control(session)
    with pytest.raises(UsageError):
        Control(session)


def test_property_access():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with Session(drone) as session:
        control = Control(session)
        assert control.access is True

    assert control.access is False


def test_property_autopilot_getter():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with Session(drone) as session1:
        control1 = Control(session1)
        assert control1.autopilot is False

    with Session(drone) as session2:
        control2 = Control(session2, autopilot=True)
        assert control2.autopilot is True


def test_property_autopilot_setter():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with Session(drone) as session:
        control = Control(session)
        assert control.autopilot is False

        control.autopilot = True
        assert control.autopilot is True


def test_property_autopilot_setter_raises():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    session = Session(drone)
    control = Control(session)
    with pytest.raises(TypeError):
        control.autopilot = Any


def test_unable_to_use_methods_if_session_finished():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    with Session(drone) as session:
        control = Control(session)

    with pytest.raises(PermissionError):
        control.takeoff()


def test_unable_to_use_methods_if_autopilot_is_turn_on():
    drone = Quadcopter('Tello', ip='192.168.10.1')
    session = Session(drone)
    control = Control(session, autopilot=True)

    with pytest.raises(PermissionError):
        control.takeoff()


@pytest.mark.parametrize('method_name', ['connect', 'disconnect', 'any'])
def test_execute_methods_raises(method_name: str):
    drone = Quadcopter('Tello', ip='192.168.10.1')
    session = Session(drone)
    control = Control(session)

    with pytest.raises(NameError):
        control.execute(method_name)
