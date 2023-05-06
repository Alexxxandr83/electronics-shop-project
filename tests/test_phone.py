from src.phone import Phone
from src.item import Item
import pytest


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert item1 + phone1 == 25


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == "iPhone 14"


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_number_of_sim():
    with pytest.raises(ValueError):
        phone1 = Phone('iPhone14', 1000, 3, 0)  # ожидаем ValueError, так как number_of_sim равно 0
        assert phone1.number_of_sim == '0'
        phone1 = Phone('iPhone14', 1000, 3, 1)  # создаем объект, number_of_sim больше 0
        assert phone1.number_of_sim == 1
