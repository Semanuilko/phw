"""
Создать скрипт, который через параметр запуска получает имя исполняемого файла.
И запускает этот файл через библиотеку subprocess. Обработку ошибок (файл не существует, или не
может быть запущен и т.д.) сделать через исключения.

Пример запуска:
python .\task04_run.py notepad
"""

import subprocess
import click


@click.command()
@click.argument('file')
def run(file):
    try:
        subprocess.run(file)
    except FileNotFoundError:
        print('Файл не существует!')
    except OSError:
        print('ошибка при попытке запуска файла!')


if __name__ == '__main__':
    run()
