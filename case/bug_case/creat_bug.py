from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
import unittest
import random


class Test_creat_bug(unittest.TestCase):

    @classmethod
    def setUpClass(self) -> None:
        self.dr = webdriver.Chrome()
        self.dr.get('http://127.0.0.1/biz/user-login.html')
        self.dr.implicitly_wait(5)
        self.dr.maximize_window()


    @classmethod
    def tearDownClass(self) -> None:
        self.dr.quit()

    def test_001_login(self):
        self.dr.find_element_by_xpath('//input[@id="account"]').send_keys('admin')
        self.dr.find_element_by_xpath('//input[@name="password"]').send_keys('123456.')
        self.dr.find_element_by_xpath('//button[@type="submit"]').click()

    def test_002_creat_bug(self):
        self.dr.find_element_by_xpath('//li[@data-id="qa"]/a').click()
        self.dr.find_element_by_link_text('Bug').click()
        self.dr.find_element_by_xpath('//a[@class="btn btn-primary"]/i').click()
        # selectObject = Select(self.dr.find_element_by_id('openedBuild'))
        # selectObject.options[0]
        self.dr.find_element_by_xpath('//ul[@class="chosen-choices"]').click()
        self.dr.find_element_by_xpath('//ul[@class="chosen-results"]/li').click()
        self.dr.find_element_by_xpath('//input[@name="title"]').send_keys('bug001')
        self.dr.execute_script('window.scrollTo(0, 1000)')
        self.dr.find_element_by_xpath('//button[@id="submit"]').click()
        sleep(3)