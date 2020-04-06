from selenium import webdriver
from time import sleep
import unittest
import random


class Test_creat_case(unittest.TestCase):

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

    def test_002_creat_case(self):
        self.dr.find_element_by_xpath('//li[@data-id="qa"]/a').click()
        self.dr.find_element_by_link_text('用例').click()
        # self.dr.find_element_by_xpath('//a[@class="btn btn-info"]').click()
        self.dr.find_element_by_xpath('//a[@class="btn btn-primary"]').click()
        self.dr.find_element_by_xpath('//ul[@class="chosen-choices"]').click()
        self.dr.find_element_by_xpath('//li[@data-option-array-index="2"]').click()
        self.dr.find_element_by_xpath('//input[@name="title"]').send_keys('test001')
        self.dr.execute_script('window.scrollTo(0,1000)')
        self.dr.find_element_by_xpath('//td[@colspan="3"]/button').click()
        sleep(4)

    def test_003_edit_case(self):
        self.dr.find_element_by_link_text('test01').click()
        self.dr.find_element_by_xpath('//div[@class="btn-toolbar"]/a[5]').click()
        self.dr.find_element_by_id('precondition').send_keys('前置条件为null')
        self.dr.find_element_by_xpath('//a[@class="chosen-single chosen-single-with-deselect"]/span').click()
        self.dr.find_element_by_xpath('//ul[@class="chosen-results"]/li[3]').click()
        self.dr.execute_script('window.scrollTo(0,1000)')
        self.dr.find_element_by_xpath('//div[@class="text-center detail form-actions"]/button').click()
