
# Sample login code using Appium and Python

## Test app I chose to use for this sample project
I am using an Android fasion app called called Poshmark.  You can easily buy and sell your fashion items in your house using this app. 


<img src="poshmark_app/poshm_login_1.png" width="200" height="400">

## Project structure 

-  screens directory (Contains page objects. I separated out locators into a different file.) https://github.com/mayukataoka/ServiceNow/tree/master/poshmark_app/screens
-  tests directory  (Contains different tests. The tests imports page objects. ) https://github.com/mayukataoka/ServiceNow/tree/master/poshmark_app/tests
-  helpers class (Contains constants.  Values can be reassigned when needed) https://github.com/mayukataoka/ServiceNow/blob/master/poshmark_app/helpers.py
-  data directory (Contains data) https://github.com/mayukataoka/ServiceNow/tree/master/poshmark_app/data
-  api directory (I did not use api today. But I usually make api calls from my Appium tests to reset state or to verify data. )

## Data driven tests for localized inputs

(Sample test 1)

Just like testNG, pytest also has a mechanism to do data driven test. Here's an example passing English, Japanese and Russion login credentails. 

```
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
```

(Sample test 2)

Similary, we can pull the login credentail data for English, Japanese and Russion from an external file. 
self.get_user_name_from_yaml_config() read a config and return data as a list of tuples just as test1 does.


```
    @pytest.mark.parametrize("username,password", self.get_user_name_from_yaml_config())
    def test_login_method2(self, driver, username, password):
        open(os.oath.join)
        login_option_screen = LoginOptions(driver)
        login_option_screen.click_login_with_email_link()

        login_screen = Login(driver)
        login_screen.login(username, password)

        assert login_screen.did_login_succeed_without_error == True
```

## Locators
https://github.com/mayukataoka/ServiceNow/blob/master/poshmark_app/screens/locators.py

