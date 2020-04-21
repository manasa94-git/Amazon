import pytest
from selenium import webdriver
@ pytest.yield_fixture(scope='function')
def setupclass():
    url="https://www.amazon.in/"
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(url)
    yield driver
    driver.implicitly_wait(20)
    driver.minimize_window()
# @pytest.fixture()
# def usersetup():



