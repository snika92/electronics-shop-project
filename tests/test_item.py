"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone
from src.item import InstantiateCSVError
import os



@pytest.fixture
def item_instance():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item_instance):
    assert item_instance.calculate_total_price() == 200000


def test_apply_discount(item_instance):
    item_instance.pay_rate = 0.8
    item_instance.apply_discount()
    assert 10000 * item_instance.pay_rate == item_instance.price
    assert item_instance.price == 8000


def test_name(item_instance):
    assert item_instance.name == "Смартфон"
    item_instance.name = "Телефон"
    assert item_instance.name == "Телефон"
    item_instance.name = "Телесмартфон"
    assert item_instance.name == "Телесмартф"


def test_instantiate_from_csv(item_instance):
    path = os.path.join("..", "src","items.csv")

    item_instance.instantiate_from_csv(path)
    assert item_instance.all[0].name == "Смартфон"


def test_instantiate_from_csv0():
    path_not_exist = os.path.join("..", "src","item.csv")
    path_without_row = os.path.join("..", "src","items_without_row.csv")

    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(path_not_exist)
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(path_without_row)


def test_string_to_number(item_instance):
    assert item_instance.string_to_number('5') == 5
    assert item_instance.string_to_number('5.0') == 5
    assert item_instance.string_to_number('5.5') == 5


def test_repr(item_instance):
    assert repr(item_instance) == "Item('Смартфон', 10000, 20)"


def test_str(item_instance):
    assert str(item_instance) == 'Смартфон'


def test_add(item_instance):
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item_instance + phone1 == 25
    assert phone1 + phone1 == 10

    with pytest.raises(ValueError):
        phone1 + 10000
