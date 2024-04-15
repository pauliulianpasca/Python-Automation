from selenium import webdriver
from assertpy import assert_that, soft_assertions


driver = webdriver.Chrome()
driver.get("https://google.com")

pageTitle = driver.title

with soft_assertions():
    assert_that(pageTitle).is_equal_to("Google")
    print(pageTitle)
    assert_that(pageTitle).is_length(6)
    assert_that(pageTitle).contains("oo") 