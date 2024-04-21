from assertpy import assert_that, soft_assertions
from locator.locators import HomeLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def goToHome(self):
        self.driver.get("https://emag.ro")
        self.driver.maximize_window()

    def verifyLogo(self):
        # Verify if the logo element is displayed
        logoButton = self.wait.until(EC.visibility_of_element_located(HomeLocators.logoButton))
        with soft_assertions():
            assert_that(logoButton).is_not_none()
            print("Logo is displayed.")
           

        # Find the logo image element using HomeLocators.logoImage locator
        logo_img = logoButton.find_element(*HomeLocators.logoImage)

        # Verify the source (URL) of the logo
        logo_src = logo_img.get_attribute("src")
        expected_logo_src = "https://s13emagst.akamaized.net/layout/ro/images/logo//59/88362.svg"

        with soft_assertions():
            assert_that(logo_src).is_equal_to(expected_logo_src)
            print("Logo source URL is correct:", logo_src)
        


        # Find the logo image element using HomeLocators.logoImage locator
        logo_img = logoButton.find_element(*HomeLocators.logoImage)

        # Verify the alt text of the logo
        alt_text = logo_img.get_attribute("alt")
        expected_alt_text = "eMAG"

        with soft_assertions():
            assert_that(alt_text).is_equal_to(expected_alt_text)
            print("Alt text of the logo is correct:", alt_text)
            

        

        # Verify the title attribute of the logo
        logo_title = logoButton.get_attribute("title")
        expected_title_part = "Căutarea nu se oprește"

        with soft_assertions():
            assert_that(logo_title).contains(expected_title_part)          
            print("Title contains expected part.")
            




    def verifyTitle(self):
      
        # Get the title of the current page
        actual_title = self.driver.title

        # Define the expected title
        expected_title = "eMAG.ro - Căutarea nu se oprește niciodată"

        # Verify if the actual title matches the expected title
        with soft_assertions():
            assert_that(actual_title).contains(expected_title)
            print("Title test passed.")
                     

        