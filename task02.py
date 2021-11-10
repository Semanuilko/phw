"""
Работа со списками, словарями и множествами
Работа с функциями
"""

# Создать список из трех любых элементов.
l = [1, 2, 'srt']

# Создать словарь из трех пар ключ-значение.
d = {'first': 'apple', 'second': 'car', 'third': 'sun'}

# Создать множество из трех элементов.
s = {1, 2, 3}

# Из списка получить элементо с индексом 1
print("0 - elem = {}".format(l[1]))

# Напиать условие if с двумя блоками elif и блоком else.
a = 12
if a < 3:
    print("a<3")
elif a < 6:
    print("a<6")
elif a < 9:
    print("a<9")
else:
    print("a>9")

# Написать цикл while.
while a > 0:
    a -= 1
    print(a)

# Создать список из трех элементов и распечать его элементы с помощью цикла for
l = ['one', 'two', 'three']
for i in range(3):
    print(l[i])

# распечатать числа от 0 до 5
for i in range(6):
    print(i)

# создать строку 'TEST', если в ней есть буква 'E', напечатать 'pass'
str = 'TEST'
if 'E' in str:
    print('pass')

# Запросить данные у пользователя и распечатать их используя форматированную строку.
s = input("Введите что-то: ")
print(f"Ввели, {s}")

# Распечатать содержимое файла.
with open('README.md', encoding='utf8') as myfile:
    for line in myfile:
        print(line)


# Создать функцию, которая принимает два аргумента, вернуть сумму двух аргументов.
def sum_fun(arg1, arg2):
    print("Summ: ", arg1 + arg2)


sum_fun(1, 2)


# Создать функцию которая принимает любое количество параметров, распечаатать эти параметры.
def any(*args):
    for arg in args:
        print(arg)


any('aaa', 'bbb', 'ccc', 'ddd')