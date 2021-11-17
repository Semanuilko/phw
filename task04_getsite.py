"""
3. Создать функцию, которая в фоновом потоке скачает содержимое сайта https://epam.com.
Скачанную информацию надо сохранить в файл.

"""
import requests


def get_site_to_file():
    r = requests.get('https://epam.com', verify=False)
    site_file = open("site_to_file.txt", "w", encoding='utf8')
    site_file.write(r.text)
    site_file.close()


get_site_to_file()
