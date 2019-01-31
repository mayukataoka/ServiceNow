import pytest
import os
from poshmark_app.helpers import EXECUTOR, PACKAGE, ACTIVITY, DEVICE
from appium import webdriver
from poshmark_app.screens.login_options_screen import LoginOptions
from poshmark_app.screens.login_screen import Login
import yaml
#import sys
#sys.path.insert(0, 'poshmark_app/data/')

class TestPoshMarkLogin():


    @pytest.mark.parametrize("username,password", [
        ("mayu", "mayuspassword"),
        ("アイウエオ", "日本語"),
        ("имя пользователя", "пароль"),
    ])
    def test_login_method1(self, driver, username, password):
        self.get_user_name_from_yaml_config()

        login_option_screen = LoginOptions(driver)
        login_option_screen.click_login_with_email_link()

        login_screen = Login(driver)
        login_screen.login(username, password)

        assert login_screen.did_login_succeed_without_error == True


    @pytest.mark.parametrize("username,password", self.get_user_name_from_yaml_config())
    def test_login_method2(self, driver, username, password):
        open(os.oath.join)
        login_option_screen = LoginOptions(driver)
        login_option_screen.click_login_with_email_link()

        login_screen = Login(driver)
        login_screen.login(username, password)

        assert login_screen.did_login_succeed_without_error == True
