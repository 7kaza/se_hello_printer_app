from selenium import webdriver
import unittest
import time
import pytest

@pytest.mark.uitest
class TestFormater(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:5000/ui")
        self.driver.maximize_window()

        time.sleep(10)

    def tearDown(self):
        self.driver.quit()

    def is_greatings_visible(self):
        wyswietla = self.driver.find_element_by_id('napis')
        print(wyswietla.text)
        self.assertEqual(wyswietla.text, "Hello World!")

    def is_name_present(self):
        wyswietl_imie = self.driver.find_element_by_id('imie')
        print(wyswietl_imie.text)
        self.assertEqual(wyswietl_imie.text, "Karolina")



def test_ui(self):
    self.driver.is_greatings_visible()
    self.driver.is_name_present()
    self.driver.is_google_integration_works()
    time.sleep(10)
    self.driver.quit()
