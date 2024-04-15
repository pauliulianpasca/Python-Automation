from assertpy import assert_that, soft_assertions
from locator.locators import AboutLocators
from selenium.webdriver.common.by import By


class AboutPage:
    def __init__(self, driver):
        self.driver = driver

    def goToAbout(self):
        self.driver.get("https://about.emag.ro/")  
        self.driver.maximize_window() 
        
    def verifyTitle(self):


    def verifyNavigation(self):