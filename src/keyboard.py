from src.item import Item


class MixinLang:
    languages = ["EN", "RU"]

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        lang = self.languages.pop(0)
        self.languages.append(lang)
        self.__language = self.languages[0]
        return self


class Keyboard(Item, MixinLang):

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
