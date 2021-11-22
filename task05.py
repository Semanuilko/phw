"""
Работа с HTML Скачать содержимое страницы https://epam.com с помощью requests
Посчитать количество тегов div на этой странице (лучше использовать для этого библиотеку beautifulsoup4)
Базы данных
Работа с sqlite. С помощью SQL запросов создать таблицу содержаюую 2 стобца:
номер и имя Добавить три строки с данными. Получить данные из таблицы и распечатать их на экране.

Если есть доступ к сетевым базам данных mysql, postgrsql можно выполнить те же операции с этими базами данных.

"""

import requests
import sqlite3
from bs4 import BeautifulSoup


def get_site():
    r = requests.get('https://epam.com', verify=False)
    return r.text


soup = BeautifulSoup(get_site(), 'html.parser')
all_div = soup.find_all("div")
print("div-ов на сайте: ", len(all_div))

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('''CREATE TABLE names
             (number int, name text)''')
c.execute("INSERT INTO names VALUES ('1','Ivan')")
c.execute("INSERT INTO names VALUES ('2','Petr')")
c.execute("INSERT INTO names VALUES ('3','Fedr')")

conn.commit()

for row in c.execute('SELECT * FROM names ORDER BY number'):
    print(row)

conn.close()
