import re
import unittest
import time
from time import sleep
from pages.SocialInsurPage import *
from pages.SocialResultPage import *
from BeautifulReport import BeautifulReport

class SocialCount(unittest.TestCase):
    """社保计算器"""
    def setUp(self):
        mobile_emulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)
        self.url = "https://apps.eshiyun.info/tools/social?geoCode=HNZMD"
        self.social_page = SocialPage(self.driver,self.url)
        self.result_page = SocialResult(self.driver, self.url)

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        """自定义社保基数-正常情况"""
        self.social_page.open()
        list = self.social_page.get_cardinal_dataY()
        sleep(0.5)
        for item in list:
            self.social_page.click(self.social_page.change_rule_loc)
            sleep(0.5)
            self.social_page.click(self.social_page.customize_loc)
            self.social_page.click(self.social_page.confer_loc)
            sleep(1)
            min = self.social_page.get_num_min()
            max = self.social_page.get_num_max()
            print("缴存基数上下限分别为：", max, min)
            self.salary = str(item['税前收入'])
            self.base_soc_fund = str(item['自定义社保基数'])
            self.social_page.input_salary(str(self.salary))
            self.social_page.input_soc_fund(str(self.base_soc_fund))
            self.social_page.click(self.social_page.count_loc)
            sleep(1)
            val1 = self.result_page.get_result(self.base_soc_fund, min, max)
            print("实际结果应为(保留一位小数)：", val1)
            val2 = self.result_page.get_pageResult()
            print("页面上结果为(保留一位小数)：", val2)
            print("-----------------------------------------")
            try:
                self.assertEqual(val1, val2, "自定义社保基数-计算结果错误！")
            except Exception as e:
                print("Test Fail!",format(e))
            self.driver.back()
            sleep(1)

    def test_2(self):
        """自定义社保基数-非正常情况"""
        self.social_page.open()
        lists = self.social_page.get_cardinal_dataN()
        sleep(0.5)
        for item in lists:
            self.social_page.rule_cardinal()
            sleep(1)
            min = self.social_page.get_num_min()
            max = self.social_page.get_num_max()
            print("缴存基数上下限分别为：", max, min)
            self.salary = str(item['税前收入'])
            self.base_soc_fund = str(item['自定义社保基数'])
            self.social_page.input_salary(str(self.salary))
            self.social_page.input_soc_fund(str(self.base_soc_fund))
            self.social_page.click(self.social_page.count_loc)
            sleep(1)
            try:
                self.driver.find_element_by_class_name("lx-toast lx-toast-center")
            except:
                print("Test Fail!")
            sleep(2)
            self.driver.refresh()




if __name__ == "__main__":
    # unittest.main()
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = now + '.html'
    case = [
        # SocialCount("test_1"),
        SocialCount("test_2")
    ]
    suit_tests = unittest.TestSuite()
    suit_tests.addTests(case)
    runner = BeautifulReport(suit_tests)
    runner.report(filename=filename,description="社保计算器测试报告",log_path='./report')