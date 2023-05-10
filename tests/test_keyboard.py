from src.keyboard import Keyboard, KeybMixin


def test_change_lang():  # Проверяем, что смена языка работает корректно
    kb = Keyboard('Test Keyboard', 900, 1)
    kb.change_lang()
    assert kb.language == 'RU'
    kb.change_lang()
    assert kb.language == 'EN'


def test_str():
    kb = Keyboard('Test Keyboard', 900, 1)
    assert str(kb) == 'Test Keyboard'

def test_keybmixin():
    kb = KeybMixin()
    assert kb._language == 'EN'
    kb.change_lang() # измененный вызов метода
    assert kb._language == "RU"
    kb.change_lang() # измененный вызов метода
    assert kb._language == "EN"