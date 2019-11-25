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
        self.url = "https://apps.eshiyun.info/tools/gjjPayment?geoCode=HNZMD"
        self.salary = 10000
        self.fund_percent = 7
        self.fund_company = 7
        self.supplement_percent = 1

    def test_1(self):
        fundcount_page = FundCalPage(self.driver,self.url, '公积金计算器')
        fundcount_page.open()
        fundcount_page.input_salary(self.salary)
        fundcount_page.input_fund_percent(self.fund_percent)
        fundcount_page.input_fund_company(self.fund_company)
        supfund_flag = fundcount_page.is_supfund_exists()
        if supfund_flag:
            fundcount_page.click_count()

            count1 = fundcount_page.count(self.salary, self.fund_percent, self.fund_company, self.supplement_percent)
            print(fundcount_page.total_loc1.getattribute('_value'))
        else:
            fundcount_page.input_sup_percent(self.supplement_percent)
            fundcount_page.click_count()


        sleep(10)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
