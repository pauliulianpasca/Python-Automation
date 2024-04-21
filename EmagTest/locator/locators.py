from selenium.webdriver.common.by import By

class HomeLocators:

    logoButton = (By.CLASS_NAME, "navbar-brand")
    logoImage = (By.TAG_NAME, 'img')
   
class AboutLocators:
    navButtons = (By.CSS_SELECTOR, "#site-header > div.container > div")
    navList = (By.TAG_NAME, "a")

