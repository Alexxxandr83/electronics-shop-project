from src.item import Item


class KeybMixin:

    def __init__(self):
        self._language = 'EN'
        super().__init__()

    def change_lang(self):
        if self._language == 'EN':
            self._language = "RU"


class Keyboard(Item, KeybMixin):

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self._language = 'EN'

    def __str__(self):
        return self.name

    def change_lang(self):
        if self.language == 'EN':
            self._language = "RU"

        else:
            self._language = "EN"
        return self

    @property
    def language(self) -> str:
        return self._language

# kb = Keyboard('Dark Project KD87A', 9600, 5)
# print(str(kb))
# print(str(kb.language))
# kb.change_lang()
# print(str(kb.language))
# # kb.language = "CH"
# # print(kb.language)
