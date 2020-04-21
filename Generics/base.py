from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep


class Generics():

    def __init__(self, driver):
        self.driver = driver

    def Getby(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == 'id':
            return By.ID
        elif locatorType == 'classname':
            return By.CLASS_NAME
        elif locatorType == 'xpath':
            return By.XPATH
        elif locatorType == 'partiallinktext':
            return By.PARTIAL_LINK_TEXT
        elif locatorType == 'linktext':
            return By.LINK_TEXT
        elif locatorType == 'csslocator':
            return By.CSS_SELECTOR
        elif locatorType == 'name':
            return By.NAME
        else:
            print("invalid loactorType", locatorType)

    def GetElement(self, locatorType, locatorValue):
        try:
            byType = self.Getby(locatorType)
            element = self.driver.find_element(byType, locatorValue)
            print("element with", locatorType, "and", locatorValue, " is found")
        except:
            print("element with", locatorType, "and", locatorValue, " not found")

        return element

    def ClickElement(self, locatorType, locatorValue):
        try:
            element = self.GetElement(locatorType, locatorValue)
            element.click()
            print("element with", locatorType, "and", locatorValue, " is clicked")
        except:
            print("element with", locatorType, "and", locatorValue, " is not clicked")

    def EnterText(self, locatorType, locatorValue, Text):
        try:
            element = self.GetElement(locatorType, locatorValue)
            element.send_keys(Text)
            print("data to", locatorType, "and", locatorValue, " is sent")

        except:
            print("data to", locatorType, "and", locatorValue, " is not sent")

    def get_elements(self, locatorType, locatorValue):
        try:
            byType = self.Getby(locatorType)
            elements = self.driver.find_element(byType, locatorValue)
            print("elements are found")
        except:
            print("element not found")

        return elements


    def wait_for_title(self, driver, time):
        wait = WebDriverWait(driver, time)
        wait.until(ec.title_is("Amazon Sign In"), "Title not matched")

        # element = self.GetElement(locatorType, locatorValue)

    def wait(self, time):
        i = 0
        while i < time:
            try:
                s = self.driver.find_element_by_xpath("'").click()
                break
            except:
                sleep(1)
                i = i + 1
