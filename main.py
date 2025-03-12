import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


os.environ['PATH'] += r"C:\Program Files\chromedriver-win32"
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")



username_enter = "standard_user"
password_enter = "secret_sauce"
username = driver.find_element(By.ID,"user-name")
username.send_keys(username_enter)
password = driver.find_element(By.ID, "password")
password.send_keys(password_enter)
log_in = driver.find_element(By.ID,"login-button")
log_in.click()

time.sleep(3)


# inventory check
add_backpack = driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
add_backpack.click()
add_bike_light = driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
add_bike_light.click()
add_tshirt = driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
add_tshirt.click()

time.sleep(3)


#remove_item
remove_item1 = driver.find_element(By.ID, "remove-sauce-labs-bike-light")
remove_item1.click()

time.sleep(3)


#check shopping cart
shopping_cart = driver.find_element(By.ID, "shopping_cart_container")
shopping_cart.click()

time.sleep(3)

#check out
check_out = driver.find_element(By.ID, "checkout")
check_out.click()

time.sleep(3)

#fill_info
name_enter = "pitnaree"
lastname_enter = "K"
postcode_enter = "w5 5ah"

name = driver.find_element(By.ID, "first-name")
name.send_keys(name_enter)
lastname = driver.find_element(By.ID, "last-name")
lastname.send_keys(lastname_enter)
postcode = driver.find_element(By.ID, "postal-code")
postcode.send_keys(postcode_enter)

time.sleep(3)

#continue
forward = driver.find_element(By.ID, "continue")
forward.click()
time.sleep(3)

#finish
finish = driver.find_element(By.ID, "finish")
finish.click()


time.sleep(100)
