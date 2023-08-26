import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard_instance():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_repr(keyboard_instance):
    assert repr(keyboard_instance) == "Keyboard('Dark Project KD87A', 9600, 5, EN)"


def test_str(keyboard_instance):
    assert str(keyboard_instance) == 'Dark Project KD87A'


def test_change_lang(keyboard_instance):
    assert str(keyboard_instance.language) == "EN"

    keyboard_instance.change_lang()
    assert str(keyboard_instance.language) == "RU"

    keyboard_instance.change_lang().change_lang()
    assert str(keyboard_instance.language) == "RU"

    with pytest.raises(AttributeError):
        keyboard_instance.language = 'CH'
