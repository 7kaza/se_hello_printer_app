#!/usr/bin/python3
import os
from selenium import webdriver
import unittest
import time
import pytest

@pytest.mark.uitest
class Hello_Printer_Website(unittest.TestCase):

    def setUp(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get('http://127.0.0.1:5000')
        time.sleep(10)

    def CheckNameAnia(self):
        driver =self.driver
        self.driver.get('http://127.0.0.1:5000/Ania')
        notices = driver.find_elements_by_xpath('//*[@id="main"]/div/section[2]/article/div/div/header/strong/h2/span')
        rv = notices.get_attribute("innerText")
        self.assertEqual("Hello Ania!", rv.data)
        time.sleep(20)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
