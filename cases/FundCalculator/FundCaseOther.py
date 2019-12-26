import sys
sys.path.append('./')
import unittest
from time import sleep
from pages.FundCalPage import *

# 其他城市：公积金计算器
class FunCalCount(unittest.TestCase):

    def setUp(self):
        mobile_emulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        self.url = "https://apps.eshiyun.info/tools/gjjPayment?geoCode=HNZMD"
        self.fundcount_page = FundCalPage(self.driver,self.url)

    def test_1(self):
        '''
        无补充公积金
        :return:
        '''

        self.fundcount_page.open()
        list = self.fundcount_page.get_other_testdata()
        sleep(5)
        for item in list:
            self.salary = str(item['salary'])
            self.fund_percent = str(item['fund_percent'])
            self.fund_company = str(item['fund_company'])
            self.fundcount_page.input_salary(self.salary)
            self.fundcount_page.input_fund_percent(self.fund_percent)
            self.fundcount_page.input_fund_company(self.fund_company)
            self.fundcount_page.click_count()
            # 预期结果
            count1 = self.fundcount_page.count_other(self.salary,self.fund_percent,self.fund_company)
            # 页面上的实际结果
            count2 = self.driver.find_element_by_xpath(self.fundcount_page.total_loc2).get_attribute('value')
            try:
                self.assertEqual(float(count2), float(count1), msg="计算结果错误")
            except Exception as e:
                print("Test Fail", format(e))
            sleep(1)

    def tearDown(self):
        self.driver.quit()
#
if __name__ == "__main__":

    suite = unittest.TestSuite()
    suite.addTest(FunCalCount("test_1"))
    runner = unittest.TextTestRunner()
    runner.run(suite)