from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get ("https://emag.ro")

"""
Locatori/Selectori

find_element() - comanda pentru a selecta

- ID
- CLASS_NAME
- TAG_NAME     - dupa importanta de sus in jos
- LINK_TEXT
- CSS_SELECTOR
- XPATH

"""


searchBox = driver.find_element(By.ID, "searchboxTrigger")

helpButton = driver.find_element(By.CLASS_NAME, "navbar-aux-help-link")

geniusLink = driver.find_element(By.LINK_TEXT, "Genius")

logo = driver.find_element(By.XPATH, "//*[@id='masthead']/div/div/div[1]/a/img")

title1 = driver.find_element(By.CSS_SELECTOR, "h2.page-section-title")
title2 = driver.find_element(By.TAG_NAME, "h2")