import re
import xlrd
import string
import unittest
from time import sleep
from selenium import webdriver
from pages.FundCalPage import *


class FunCalCount(unittest.TestCase):

    def setUp(self):
        mobile_emulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        self.url = "https://apps.eshiyun.info/tools/gjjPayment?geoCode=SHS"
        self.salary = 10043
        self.fund_percent = 7
        self.fund_company = 7
        self.supplement_percent = 1

    def test_1(self):
        '''
        有补充公积金
        :return:
        '''
        fundcount_page = FundCalPage(self.driver,self.url, '公积金计算器')
        fundcount_page.open()
        fundcount_page.input_salary(self.salary)
        fundcount_page.input_fund_percent(self.fund_percent)
        fundcount_page.input_fund_company(self.fund_company)
        try:
            fundcount_page.input_sup_percent(self.supplement_percent)
        except Exception as e:
            print("该城市计算器无补充公积金", format(e))
        fundcount_page.click_count()

        count1 = fundcount_page.count(self.salary, self.fund_percent, self.fund_company, self.supplement_percent)
        count2 = self.driver.find_element_by_xpath(fundcount_page.total_loc2).get_attribute('value')
        try:
            self.assertEqual(float(count2), float(count1), msg="计算结果错误")
        except Exception as e:
            print("Test Fail", format(e))
        sleep(10)

    def tearDown(self):
        self.driver.quit()
#
if __name__ == "__main__":
    unittest.main()
