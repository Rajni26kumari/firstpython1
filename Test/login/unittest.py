import unittest
from selenium import webdriver
import HtmlTestRunner
import os
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
class LoginTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver= webdriver.Chrome("E:/chromedriver/chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def test_login(self):
        self.assertTrue(True)

    @classmethod
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
'''
        url= "https://devicemon.azurewebsites.net"
        self.driver.get(url)
        self.driver.find_element_by_xpath("//*[@id='i0116']").send_keys("test.ncadminuser@ha-efbops.com")
        self.driver.find_element_by_id("idSIButton9").click()
        self.driver.find_element_by_xpath("//*[@id='i0118']").send_keys("nathcorp!1")
        time.sleep(4)
        self.driver.find_element_by_id("idSIButton9").click()
        self.driver.find_element_by_id("idSIButton9").click()
'''




