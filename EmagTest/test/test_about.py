import sys
sys.path.append(r"C:\Users\kavi\Documents\Python-Automation\EmagTest")

from selenium import webdriver
import unittest
from page.about_page import AboutPage as AP


class ProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_aboutNav(self):
        aboutPage = AP(self.driver)
        aboutPage.goToAbout()
        aboutPage.verifyNavigation()


    def test_title(self):
        aboutPage = AP(self.driver)
        aboutPage.goToAbout()
        aboutPage.verifyTitle()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()    