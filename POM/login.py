
from Generics.base import Generics
from selenium.webdriver.common import action_chains

class Log_in(Generics):

    def __init__(self,driver):

        self.driver=driver
        super().__init__(driver)

    signin = "(//span[@class='nav-line-1'])[2]"
    url= "https://www.amazon.in/"

    def signIn(self):
        # self.driver.get(self.url)
        # self.driver.maximize_window()
        self.ClickElement("xpath",self.signin)




