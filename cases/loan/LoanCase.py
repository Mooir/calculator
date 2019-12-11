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
        mobile_emulation = {'deviceName': 'Pixel 2'}
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
        """公积金贷款"""
        self.loan_page.open()
        list = self.loan_page.get_acc_testdata()
        for item in list:
            acc_count = str(item['贷款金额'])
            acc_year = str(item['贷款年限'])
            self.loan_page.input_acc_count(acc_count)
            self.loan_page.select_year(acc_year)
            sleep(0.5)
            self.loan_page.select_acc_rate()                #随机选择贷款利率
            sleep(0.5)
            y_acc_rate = self.loan_page.get_acc_rate()
            #计算结果
            result1 = self.loan_page.repay_equal_interest(float(acc_count), float(y_acc_rate), float(acc_year))
            self.loan_page.click_count()
            sleep(1)
            #页面上实际结果
            total_repay = self.result_page.get_total_repay()
            print("页面上结果为:", total_repay, "计算结果为:", result1)
            try:
                self.assertEqual(total_repay, result1, msg="计算结果错误")
            except Exception as e:
                print("Test Fail!", format(e))
            self.driver.back()
        sleep(5)
    def test_2(self):
        """商业贷款"""
        self.loan_page.open()
        
        list = self.loan_page.get_buss_testdata()
        for item in list:
            self.loan_page.select_acc_rate()
            sleep(0.5)
            self.loan_page.select_tab_buss()
            buss_count = str(item['贷款金额'])
            buss_year = str(item['贷款年限'])
            self.loan_page.input_buss_count(buss_count)
            self.loan_page.select_year(buss_year)
            sleep(0.5)
            self.loan_page.select_buss_rate()
            sleep(10)
            self.loan_page.click_count()
            self.driver.back()

        sleep(5)


if __name__ == "__main__":
    # unittest.main()
    suit = unittest.TestSuite()
    cases = [
        LoanCount("test_1"),
        # LoanCount("test_2")
    ]
    suit.addTests(cases)
    runne = unittest.TextTestRunner()
    runne.run(suit)