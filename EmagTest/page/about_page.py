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
        # Get the actual title of the page
        actual_title = self.driver.title

        # Verify if the actual title contains "eMAG Teams"
        with soft_assertions():
            assert_that(actual_title).contains("Bine ai venit la eMAG")

        # Determine whether the assertion passed or failed

        if assert_that(actual_title).contains("Bine ai venit la eMAG"):
            print("Title test passed.")
        else:
            print("Title test failed.")
        
    

    def verifyNavigation(self):
        # Find the navigation buttons container
        navButtons = self.driver.find_element(*AboutLocators.navButtons)

        # Find all navigation buttons within the container
        navList = navButtons.find_elements(*AboutLocators.navList)

        # Extract the text of each navigation button
        navButtonText = [button.text for button in navList]
        for text in navButtonText:
            print(text)
           
        # Verify the navigation buttons
        with soft_assertions():
            
            if assert_that(navButtonText).contains("Grupul eMAG", "eMAG Teams", "Sustenabilitate", "Media"):
                
                print("Butoanele sunt corecte.", text)
            else:
                print("Nu am gasit butoanele.")
        