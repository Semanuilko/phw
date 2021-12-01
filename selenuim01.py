import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(5)
driver.get('https://esia-portal1.test.gosuslugi.ru')


inputs = driver.find_elements_by_xpath('//input')

for input_elem in inputs:
    if input_elem.get_attribute('type') != 'hidden':
        input_elem.send_keys('test')
        print(input_elem.get_attribute('type'))

driver.quit()