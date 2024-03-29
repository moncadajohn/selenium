import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.keys import Keys


class newTours(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r"E:\drivers\chrome\chromedriver.exe")
        self.driver.get("http://newtours.demoaut.com/")
        time.sleep(5)


#Lo que queda en medio son los casos de prueba
#cada caso de prueba es un método aparte
#y cada método debe empezar con la palabra test
    def test_dropdown(self):
        self.driver.find_element_by_link_text('REGISTER').click()
        countryDropDown = Select(self.driver.find_element_by_name("country"))
        countryDropDown.select_by_index(5)
        countryDropDown.select_by_value("11")
        countryDropDown.select_by_visible_text("CONGO")
        self.assertEquals(countryDropDown.first_selected_option.text.strip(),"CONGO")

    def test_register(self):
        user_box = self.driver.find_element_by_name("userName")
        pass_box = self.driver.find_element_by_name("password")
        submit_button = self.driver.find_element_by_name("login")
        user_box.send_keys('test')
        pass_box.send_keys('test')
        submit_button.click()
        time.sleep(3)
        link_registration_form = self.driver.find_element_by_link_text("registration form")
        self.assertEquals(link_registration_form.text,"registration form")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
	unittest.main()	