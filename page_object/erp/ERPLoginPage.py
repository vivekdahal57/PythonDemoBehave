from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
# from page_object.locators import ERPLoginPage


class ERPLoginPage(BasePage):
    login_button = (By.XPATH, '//button[contains(text(),\'Login\')]')
    login_title_text = (By.XPATH, '//h1[contains(text(),\'Login\')]')
    username_field = (By.XPATH, '//p[contains(text(),\'Username\')]/parent::label/input')
    password_field = (By.XPATH, '//p[contains(text(),\'Password\')]/parent::label/input')
    incorrect_login_message = (By.XPATH, '/html[1]/body[1]/aside[1]/div[1]/div[2]/p[1]')

    def __init__(self, obj):
        self._web_driver = obj

    def verify_login_page(self):
        self._web_driver.find_element(self.login_title_text)

    def login(self, username, password):
        if username != '' and password != '':
            self._web_driver.send_value(self.username_field, username)
            self._web_driver.send_value(self.password_field, password)
        self._web_driver.click_element(self.login_button)

    def verify_login_fail(self):
        try:
            self._web_driver.verify_text(self.incorrect_login_message, 'Incorrect email and/or password.', 2)
        except TimeoutException:
            self.verify_login_page()
