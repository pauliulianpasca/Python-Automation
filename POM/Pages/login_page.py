from selenium.webdriver.common.by import By
from assertpy import assert_that, soft_assertions
from locators.locators import LoginLocator

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def goToLogin(self):
         self.driver.get("https://practicetestautomation.com/practice-test-login/")
         self.driver.maximize_window() 
    def setUsername(self, userVal):
        username = self.driver.find_element(*LoginLocator.username)
        username.clear()
        username.send_keys(userVal)

    def setPassword(self, passVal): 
        username = self.driver.find_element(*LoginLocator.password)
        username.clear()
        username.send_keys(passVal)
    
    def clickSubmit(self):
        submitButton = self.driver.find_element(*LoginLocator.submit)
        submitButton.click()

    def verifyLoginTitle(self):
        title = self.driver.find_element(*LoginLocator.loginTitle)
        with soft_assertions():
            assert_that(title).is_true()