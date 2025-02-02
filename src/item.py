import csv
import os


class InstantiateCSVError(Exception):
    pass


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
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__name, self.price, self.quantity}'

    def __str__(self):
        return self.__name

    def __add__(self, other):
          """
    Метод, выполняющий сложение двух объектов.

    :param other: Второй объект, с которым выполняется сложение.
    :type other: object
    :return: Сумма количества текущего объекта и количества другого объекта.
    :rtype: int
    """
        if isinstance(self, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            return print('Длина наименования товара превышает 10 символов')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""
        file_path = os.path.join(os.path.dirname(__file__), 'items.csv')
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        item = cls(row['name'], cls.string_to_number(row['price']), int(row['quantity']))
                    except ValueError:
                        raise InstantiateCSVError("Файл items.csv поврежден")
                    cls.all.append(item)
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")

    @staticmethod
  """
    Преобразует строковое значение в число.

    Аргументы:
    - value (str): Строковое значение, которое нужно преобразовать в число.

    Возвращает:
    - int: Числовое значение, полученное после преобразования строки.

    Пример использования:
    >>> string_to_number("3.14")
    3
    """
    def string_to_number(value):
        return int(float(value))
