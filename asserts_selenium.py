#asserts, si algo falla corta la prueba

import time
from selenium import webdriver
driver = webdriver.Chrome('E:\drivers\chrome\chromedriver.exe')
driver.get('http://newtours.demoaut.com/')

time.sleep(5)

#identificación de elementos
user_box = driver.find_element_by_name('userName')
pass_box = driver.find_element_by_name('password')
submit_button = driver.find_element_by_name('login')

#interacción de elementos
user_box.send_keys('test')
pass_box.send_keys('test')
submit_button.click()
time.sleep(5)

#link
link_registration = driver.find_element_by_link_text("registration form")
assert link_registration.text=="registration form"
assert link_registration.tag_name =="a"
driver.quit()

