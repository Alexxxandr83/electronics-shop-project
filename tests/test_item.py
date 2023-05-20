"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item
from src.phone import Phone
import csv
import os

item1 = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 200000.0


def test_name_setter():
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара равна 10 символов
    item.name = '0123456789'
    assert item.name == '0123456789'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item.name != 'СуперСмартфон'


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.0") == 5
    assert Item.string_to_number("5.5") == 5


def test_instantiate_from_csv():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()
    Item.all.clear()
    try:
        Item.instantiate_from_csv()
    except InstantiateCSVError:
        pass
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].name == "Ноутбук"


class InstantiateCSVError(Exception):
    pass


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
