import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone_instance():
    return Phone("iPhone 14", 120000, 5, 2)


def test_repr(phone_instance):
    assert repr(phone_instance) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone_instance):
    assert str(phone_instance) == 'iPhone 14'


def test_number_of_sim(phone_instance):
    assert phone_instance.number_of_sim == 2
    phone_instance.number_of_sim = 1
    assert phone_instance.number_of_sim == 1

    with pytest.raises(ValueError):
        phone_instance.number_of_sim = 0
