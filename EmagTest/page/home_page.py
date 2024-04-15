from assertpy import assert_that, soft_assertions
from locator.locators import HomeLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def goToHome(self):
         self.driver.get("https://emag.ro")
         self.driver.maximize_window()

    def verifyLogo(self):


    def verifyTitle(self):