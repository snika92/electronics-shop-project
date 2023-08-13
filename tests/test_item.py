"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


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


def test_name(item_instance):
    item_instance.name = "Телефон"
    assert item_instance.name == "Телефон"
    item_instance.name = "Телесмартфон"
    assert item_instance.name == "Телесмартф"


# Тест отрабатывает в pycharm, а в терминале выводит ошибку
# "Нет такого файла или директории"
#
# def test_instantiate_from_csv(item_instance):
#     item_instance.instantiate_from_csv()
#     assert len(Item.all) == 6


def test_string_to_number(item_instance):
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
