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
driver.quit()


