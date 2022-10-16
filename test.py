from selenium import webdriver
from selenium.webdriver.common.keys import Keys


user_name = ""
password = ""
#driver = webdriver.Firefox()
driver.get("https://demo.thingsboard.io/login")
element = driver.find_element(By.id("username-input"))
element.send_keys(user_name)
element = driver.find_element(By.id("password-input"))
element.send_keys(password)
element.send_keys(Keys.RETURN)
element.close()
