from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

#Aduce o pagina
driver.get("https://google.com")
driver.maximize_window()

#driver.implicitly_wait(10) 

#Click pe un element din pagina

#buttonLogin = driver.find_element(By.ID, "login_button")
buttonLogin = wait.until(EC.presence_of_element_located(By.ID, "login_button"))
buttonLogin.click()


#Scriem test sau apasam un buton de la tastatura

userImput = driver.find_element(By.ID, "user_imput")
userImput.send_keys("Abc paul 123")
userImput.send_keys(Keys.ENTER)

# Cum interactionam cu un select box

countryDropdown = driver.find_element(By.ID, "user_dropdown")
countryDropdown.select_by_value("Romania")
countryDropdown.select_by_index(185)

#time.sleep(5) #Delay Doar in cazuri urgente daca facem debug  daca este nevoie de o asteptare

driver.close() # inchide pagina curenta in case se tine testul
driver.quit() # inchide tot browser-ul(omoara tot) - mai recomandat, memoria nu se incarca
