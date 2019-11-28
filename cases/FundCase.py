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
        self.salary = 10000
        self.fund_percent = 9
        self.fund_company = 9
        self.supplement_percent = 8

    def test_1(self):
        '''
        有补充公积金
        :return:
        '''
        filename = u"C:/code/calculator/cases/testcase.xlsx"
        sheetname = u'Sheet1'

        # filename = u"C:/code/calculator/cases/testcase.xlsx"
        # work = xlrd.open_workbook(filename)
        # sheet = work.sheet_by_name("Sheet1")
        # print("总共有{lines}".format(lines = sheet.nrows))
        # print("总共有{cols}".format(cols=sheet.ncols))
        # for line  in range(0,sheet.nrows):
        #     salary, fund_persent, fund_company,sup_fun = sheet.row_values(line)
        #     print(salary, fund_persent, fund_company,sup_fun)
        fundcount_page = FundCalPage(self.driver,self.url, '公积金计算器')
        list = fundcount_page.get_testdata()
        print(list)
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
        count2 = self.driver.find_element_by_xpath(fundcount_page.total_loc1).get_attribute('value')
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
