from selenium import webdriver
import path_config #Nu uita sa modifici path-ul in fisierul path_config.py cu folderul proiectului tau
import unittest
from page.about_page import AboutPage as AP


class ProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_aboutNav(self):


    def test_title(self):


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()    