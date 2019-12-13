import re
import unittest
import time
import sys
sys.path.append('C:\\code\\calculator')
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
        self.url = "https://apps.eshiyun.info/tools/social?geoCode=SHS"
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
            print("实际结果应为(取整)：", val1)
            val2 = self.result_page.get_pageResult()
            print("页面上结果为(取整)：", val2)
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
            flag = self.social_page.isElementPresent()
            if flag is True:
                print("有toast提示，测试通过")
            else:
                print("Test Fail")
            sleep(2)
            self.driver.refresh()

    def test_3(self):
        """按税前工资缴纳"""
        self.social_page.open()
        lists = self.social_page.get_default_data()
        # print(lists)
        self.social_page.rule_cardinal()
        min = self.social_page.get_num_min()
        max = self.social_page.get_num_max()
        sleep(0.5)
        self.social_page.rule_default()
        # sleep(0.5)
        print("缴纳基数上下限分别为",max,min)
        for item in lists:
            self.salary = str(item["税前工资"])
            self.social_page.input_salary(self.salary)
            self.social_page.click(self.social_page.count_loc)
            sleep(0.5)
            val1 = self.result_page.get_result(self.salary, min, max)
            print("实际结果应为(取整)：", val1)
            val2 = self.result_page.get_pageResult()
            print("页面上结果为(取整)：", val2)
            print("-----------------------------------------")
            try:
                self.assertEqual(val1, val2, "按税前工资缴纳-计算结果错误！")
            except Exception as e:
                print("Test Fail!", format(e))
            self.driver.back()
            sleep(1)        
    def test_4(self):
        """按最低基数缴纳"""
        self.social_page.open()
        list = self.social_page.get_lowest_data()
        # print(list)
        self.social_page.rule_cardinal()
        min = self.social_page.get_num_min()
        
        print("最低缴纳基数为：",min)
        for item in list:
            self.social_page.rule_lowest()
            self.salary = str(item["税前工资"])
            self.social_page.input_salary(self.salary)
            self.social_page.click(self.social_page.count_loc)
            sleep(0.5)
            val1 = self.result_page.get_result_lowest(min)
            val2 = self.result_page.get_pageResult()
            print("-----------------------------------------")
            print("实际结果应为：", val1)
            print("页面上结果为：", val2)
            try:
                self.assertEqual(val1, val2,"按最低基数缴纳-计算结果错误")
            except Exception as e:
                print("Test Fail", format(e))
            self.driver.back()
            sleep(1)



if __name__ == "__main__":
    # unittest.main()
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = now + '.html'
    case = [
        SocialCount("test_1"),
        SocialCount("test_2"),
        SocialCount("test_3"),
        SocialCount("test_4")
    ]
    suit_tests = unittest.TestSuite()
    suit_tests.addTests(case)
    runner = BeautifulReport(suit_tests)
    runner.report(filename=filename,description="社保计算器测试报告",log_path='./report')
    # run = unittest.TextTestRunner()
    # run.run(suit_tests)