from POM.login import Log_in
from selenium import webdriver
from POM.signin import SignIn
import pytest
import unittest

@pytest.mark.usefixtures('setupclass')
class TestDemoOne(unittest.TestCase):

    # filepath = "C:/Users/admin/Desktop/testdata.xlsx"

    @pytest.fixture(autouse=True)
    def classsetup(self,setupclass):
        self.lp = Log_in(self.driver)
        self.si = SignIn(self.driver)

    def test_one(self):
        self.lp.signIn()
        self.si.amazonSignIn(self.driver)
#
# driver=webdriver.Chrome()
# LP=Log_in(driver)
# Sp=SignIn(driver)
# LP.signIn()
# Sp.amazonSignIn(driver)

