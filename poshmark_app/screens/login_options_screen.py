
from poshmark_app.screens.locators import Locators

class LoginOptions:

    def __init__(self, driver):
        self.driver = driver

    def click_login_with_email_link(self):
        self.driver.find_element_by_id(Locators.login_with_email_id).click()
