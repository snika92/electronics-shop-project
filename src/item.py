import csv


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.message = "Файл item.csv поврежден"

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.price = price
        self.quantity = quantity
        self.__name = name
        super().__init__()

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_string):
        if len(name_string) > 10:
            self.__name = name_string[:10]
        else:
            self.__name = name_string

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, path):
        try:
            with open(path) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                rows = reader.fieldnames
                expected_rows = ["name", "price", "quantity"]
                for row in expected_rows:
                    if row not in rows:
                        raise InstantiateCSVError
                for line in reader:
                    item = cls(line['name'], line['price'], line['quantity'])
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(number):
        numbers = number.split(".")
        return int(number[0])

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return int(self.quantity) + int(other.quantity)
        raise ValueError("Складывать можно только объекты Item и дочерние от них")
