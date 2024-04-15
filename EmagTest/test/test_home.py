from selenium import webdriver
import path_config
import unittest
from page.home_page import HomePage as HP

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_logo(self):


    def test_title(self):


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()    