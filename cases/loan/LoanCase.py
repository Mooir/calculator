import re
import time
import unittest
from selenium import webdriver
from time import sleep
from pages.LoanPage import *
from pages.LoanResultPage import *

class LoanCount(unittest.TestCase):
    """贷款计算器"""
    def setUp(self):
        mobile_emulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.url = "https://apps.eshiyun.info/tools/"
        self.loan_page = LoanPage(self.driver,self.url)
        self.result_page = LoanResultPage(self.driver, self.url)

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        self.loan_page.open()
        val = self.loan_page.get_value_year()
        acc_rate = self.loan_page.get_acc_rate()
        print(acc_rate,type(acc_rate))
        # self.driver.find_elements_by_class_name()
        self.loan_page.select_year(29)
        sleep(5)

if __name__ == "__main__":
    unittest.main()