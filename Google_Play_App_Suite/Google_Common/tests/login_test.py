import pytest
import os
from poshmark_app.screens.login_screen import Login


class GoogleLogin():

    @pytest.mark.parametrize("username,password", self.get_user_name_from_yaml_config())
    def test_login_method(self, driver, username, password):
        open(os.oath.join)
        login_screen = Login(driver)
        login_screen.login(username, password)
        assert login_screen.did_login_succeed_without_error == True
