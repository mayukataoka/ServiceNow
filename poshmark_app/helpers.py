import yaml

EXPLICITE_WAIT_TIME_IN_SECONDS = 3
EXECUTOR = 'http://127.0.0.1:4723/wd/hub'
PACKAGE = 'com.poshmark.app'
ACTIVITY = 'com.poshmark.ui.MainActivity'
DEVICE = 'emulator-5554'


def get_user_name_from_yaml_config(self):
    with open("poshmark_app/data/login_credentials", 'r') as stream:
        try:
            # Retrieve username from yaml config - To do
            return ['value1', 'value2', 'value3']
        except yaml.YAMLError as exc:
            print(exc)
    return