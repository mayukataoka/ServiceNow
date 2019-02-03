from poshmark_app.screens.locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Login:
    delay = 3  # seconds

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element_by_id(Locators.username_id).send_keys(username)
        self.driver.find_element_by_id(Locators.password_id).send_keys(password)
        self.driver.find_element_by_id(Locators.login_button_id).click()

    def did_login_succeed_without_error(self):
        try:
            delay = 1  # seconds
            element = WebDriverWait(self.driver,delay).until(
            EC.visibility_of_element_located((By.ID, Locators.captcha_checkbox_id)))
            return True
        except TimeoutException:
            return False

