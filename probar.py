import unittest
from selenium import webdriver
class SearchText(unittest.TestCase):
	def setUp(self):
    # crea la sesion con firefox
	    self.driver = webdriver.Chrome(executable_path=r'E:\drivers\chrome\chromedriver.exe')
	    self.driver.implicitly_wait(30)
	    self.driver.maximize_window()
	    # navega hasta esa url
	    self.driver.get("http://www.google.com/")