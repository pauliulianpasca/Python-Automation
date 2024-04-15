from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from assertpy import soft_assertions, assert_that
import unittest

class LoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://practicetestautomation.com/practice-test-login/")

    def test_login(self):
        wait = WebDriverWait(self.driver, 10)

        username = self.driver.find_element(By.ID, "username")
        password = self.driver.find_element(By.ID, "password")
        submitButton = self.driver.find_element(By.ID, "submit")

        username.send_keys("student")
        password.send_keys("Password123")
        submitButton.click()

        title = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1.post-title"))) 

        #title = driver.find_element(By.CSS_SELECTOR, "h1.post-title")

        with soft_assertions():
            assert_that(title).is_true()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()