import pytest
from appium import webdriver
from poshmark_app.helpers import EXECUTOR, PACKAGE, ACTIVITY, DEVICE
from appium import webdriver

@pytest.fixture(scope="class", autouse=True)
def driver(request):
    driver = webdriver.Remote(
        command_executor=EXECUTOR,
        desired_capabilities={
            'appPackage': PACKAGE,
            'appActivity': ACTIVITY,
            'platformName': 'Android',
            'automationName': 'UIAutomator2',
            'deviceName': DEVICE,
        }
    )

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    driver.implicitly_wait(10)
    return driver