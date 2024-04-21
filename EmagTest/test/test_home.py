import sys
sys.path.append(r"C:\Users\kavi\Documents\Python-Automation\EmagTest")

from selenium import webdriver
import unittest
from page.home_page import HomePage as HP

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_logo(self):

        homePage = HP(self.driver)
        homePage.goToHome()
        homePage.verifyLogo()


    def test_title(self):

        homePage = HP(self.driver)
        homePage.goToHome()
        homePage.verifyTitle()


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()    


 