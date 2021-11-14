"""
Классы, перехват ошибок
"""


# Создать класс в конструктор которого передается одно число
# В этом классе дожен быть метод show, который распечатывает переданное число.
from collections import namedtuple


class Number:
    def __init__(self, number):  # конструктор
        # self – это экземпляр
        self.number = number

    def show(self):
        print(self.number)


n1 = Number(2)
n1.show()


# Создать класс, который наследуется от предыдущего класса и в этот класс передается два числа.
# Данный класс реализует метод calc, который складывает эти два числа.

class Second(Number):
    def __init__(self, number, second):
        self.second = second
        super().__init__(number)

    def calc(self):
        return self.number + self.second


s1 = Second(1, 4)
print(s1.calc())

# Создать блок try/except/finally Внутри блока try создать выражение, которое делит на 0.
# Перехватить эту ошибку и распечатать сообщение пользвоателю.

try:
    a = 10 / 0
    print("All fine")
except ZeroDivisionError as error:
    print("Внимание! Деление на 0 ", error)
finally:
    print("In finally block")


# Создать декоратор, который перед запуском функции распечатывает все аргументы вызываемой функции.

def trace(func):
    def inner(*args):
        print('аргументы ', args)
        return func(*args)

    return inner


@trace
def foo(x, y):
    print(x + y)


foo(1, 2)


# Создать класс в котором применить декоартор @property для доступа к внутренней переменной.

class Decor:
    def __init__(self, value):
        self._data = value

    @property
    def data(self):
        return self._data


d = Decor(3)
print('Декоратор ', d.data)


# Создать генератор который возвращается числа от 1 до 10

def first_gen():
    b = 1
    while b <= 10:
        yield b
        b += 1


for g in first_gen():
    print(g)

# С помощью стандартной функции collections.namedtuple создать объект для хранения точки в трехмерном пространстве.

Point = namedtuple('Point', 'x y z')
pt1 = Point(1.0, 5.0, 2.0)
print(pt1)


# Создать пакет в котором будет функция для распечатки текущей даты (можно использовать пакет datetime).
# Для данного пакета подготовить setup.py для установки.

# Смотри каталог printdate

