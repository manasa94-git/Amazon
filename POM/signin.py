from Generics.base import Generics
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class SignIn(Generics):
    # -----variables with attribute value-----------------------------
    logIn_Input = "//input[@id='ap_email']"
    Continue_button = "continue"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def amazonSignIn(self, driver):
        self.wait_for_title(driver,10)
        # self.ClickElement("xpath", self.logIn_Input)
        # sleep(1)
        self.EnterText("xpath", self.logIn_Input, "8088905150")
        self.ClickElement("id", self.Continue_button)
