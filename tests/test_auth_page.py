import time

from pages.auth_page import AuthPage
from pages.profile_page import ProfilePage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(ChromeDriverManager().install())
auth_page = AuthPage(driver=driver)
auth_page.open()
# time.sleep(10)
auth_page.get_element('ID', 'login').send_keys('9999')
auth_page.get_element('ID', 'password').send_keys('9999')
auth_page.get_element('ID', 'loginByPwdButton', 5).click()

assert auth_page.text_is_displayed('Введите телефон, почту или СНИЛС')

auth_page.get_element('ID', 'login').clear()
auth_page.get_element('ID', 'password').clear()
auth_page.get_element('ID', 'login').send_keys('000-000-600 01 ')
auth_page.get_element('ID', 'password').send_keys('qwe')
auth_page.get_element('ID', 'loginByPwdButton', 5).click()

assert auth_page.text_is_displayed('Введен неверный логин или пароль')

auth_page.get_element('ID', 'login').clear()
auth_page.get_element('ID', 'password').clear()
auth_page.get_element('ID', 'login').send_keys('000-000-600 01 ')
auth_page.get_element('ID', 'password').send_keys('11111111')
auth_page.get_element('ID', 'loginByPwdButton', 10).click()

profile_page = ProfilePage(driver=driver)
profile_page.open()

assert profile_page.text_is_displayed('Мужской')

# auth_page.fill_login_input('login')
# auth_page.fill_pwd_input('pwd')
time.sleep(10)
