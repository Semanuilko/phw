"""
2. Написать функцию, которая распечатает все файлы в каталоге. В функцию добавить вывод отладочной
информации через библиотеку logging (указать какой каталог обрабатывается и сколько файлов в каталоге
было распечатано).
"""

import os
import logging
import sys


def get_dir_files():
    logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(stream=sys.stdout)
    list_dir = os.listdir()
    files = []
    logging.info("Обрабатывается каталог " + os.getcwd())

    for file in list_dir:
        if os.path.isfile(file):
            files.append(file)

    logging.info("Распечатано файлов: " + str(len(files)))
    print(files)


get_dir_files()