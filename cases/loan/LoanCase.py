import re
import sys
import time
import unittest
from selenium import webdriver
from time import sleep
sys.path.append('C:\\code\\calculator')
from pages.LoanPage import *
from pages.LoanResultPage import *


class LoanCount(unittest.TestCase):
    """贷款计算器"""
    def setUp(self):
        mobile_emulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        # options.set_headless()#浏览器无头模式
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.url = "https://apps.eshiyun.info/tools/"
        self.loan_page = LoanPage(self.driver,self.url)
        self.result_page = LoanResultPage(self.driver, self.url)

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        self.loan_page.open()
        # val = self.loan_page.get_value_year()
        # acc_rate = self.loan_page.get_acc_rate()
        # print(acc_rate, type(acc_rate))
        # self.driver.find_elements_by_class_name()
        list = self.loan_page.get_acc_testdata()
        result = self.loan_page.equal_corpus(30, 10, 0.0325)
        print(result)
        for item in list:
            self.acc_count = str(item['贷款金额'])
            self.acc_year = str(item['贷款年限'])
            self.loan_page.input_acc_count(self.acc_count)
            self.loan_page.select_year(self.acc_year)
            sleep(0.5)
            self.loan_page.select_acc_rate()#随机
            sleep(0.5)
            self.loan_page.click_count()
            sleep(1)
            self.driver.back()
        sleep(5)


if __name__ == "__main__":
    unittest.main()