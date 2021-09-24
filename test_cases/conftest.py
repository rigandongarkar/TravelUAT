import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    BrowserName = request.config.getoption("browser")
    if BrowserName == "chrome":
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument("--start-maximized")
        driver = webdriver.Chrome(executable_path="E:\\python selenium\\chromedriver_win32\\chromedriver",
                                  options=chromeOptions)
        # driver.maximize_window
        driver.get("https://www.phptravels.net/")
        driver.implicitly_wait(10)
    # if BrowserName == "firefox":
    request.cls.driver = driver
    yield
    driver.close()
