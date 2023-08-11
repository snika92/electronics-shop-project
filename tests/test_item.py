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
