from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
from time import sleep
class Getfile(unittest.TestCase):
    def chushi(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.python.org')
        self.driver.maximize_window()

    def getpython(self):
        self.driver.find_element_by_name("q").send_keys("python")
        self.driver.find_element_by_id("submit").send_keys(Keys.ENTER)

    def end(self):
        print('test is over')
        print(self.driver.page_source)

if __name__=="__main__":
    unittest.main()






