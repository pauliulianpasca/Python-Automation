import sys
sys.path.append(r"C:\Users\kavi\Documents\Python-Automation\POM")



from selenium import webdriver
import unittest
from Pages.login_page import LoginPage as LP

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_login(self):
        loginPage = LP(self.driver)

        loginPage.goToLogin()
        loginPage.setUsername("student")
        loginPage.setPassword("Password123")
        loginPage.clickSubmit()
        loginPage.verifyLoginTitle()


    



    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()