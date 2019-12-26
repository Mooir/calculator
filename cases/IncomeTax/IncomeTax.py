import re
import sys
import time
import unittest
from BeautifulReport import BeautifulReport
from selenium import webdriver
from time import sleep
sys.path.append('./')
from pages.TaxPage import TaxPage
from pages.ChoiceCityPage import ChCityPage
from pages.DeductionItemsPage import DeItemPage
from pages.ResultSalaryPage import RSalaryPage
from pages.ResultBounsPage import BounsTax


class IncomeTax(unittest.TestCase):
    """个税计算器"""
    def setUp(self):
        mobile_emulation = {'deviceName': 'Pixel 2'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        # options.set_headless()#浏览器无头模式
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(10)
        self.url = "https://apps.eshiyun.info/tools/Tax2?geoCode=SHS"
        self.tax_page = TaxPage(self.driver,self.url)
        self.city_page = ChCityPage(self.driver, self.url)
        self.deItem_page = DeItemPage(self.driver, self.url)
        self.result_page = RSalaryPage(self.driver, self.url)
        self.bounsTax_page = BounsTax(self.driver, self.url)

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        """切换城市-驻马店"""
        city_input = 'ZMD'
        self.tax_page.open(self.url)
        self.tax_page.click_city()
        self.city_page.select_city(city_input)
        sleep(0.5)
        city_text = self.tax_page.get_city()
        try:
            self.assertEqual(city_text, '河南驻马店', msg='切换城市出错')
        except Exception as e:
            raise Exception("Test Fail!", format(e))

    def test_2(self):
        """选择月份"""
        month_input = 10
        self.tax_page.open(self.url)
        self.tax_page.select_month(month_input)
        month = self.tax_page.get_month()
        try:
            self.assertIn(str(month_input), month, msg="选择月份出错")
        except Exception as e:
            print("Test Fail!", format(e))

    def test_3(self):
        """修改五险一金"""
        self.tax_page.open(self.url)
        self.tax_page.input_salary(20000)
        fundcal_past = self.tax_page.get_fundcal()
        fundcal_new = self.tax_page.modify_fundcal(10000, 10000, 7, 1)
        try:
            self.assertIsNot(fundcal_past, fundcal_new, msg="修改五险一金未修改成功")
        except Exception as e:
            print("Test Fail!", format(e))

    def test_4(self):
        """专项附加扣除"""
        self.tax_page.open(self.url)
        self.tax_page.click_deItems()
        self.deItem_page.check_hosing_loan()
        decount_modify = self.deItem_page.get_total_decrease()
        self.deItem_page.click_save()
        sleep(0.5)
        decount_show = self.tax_page.get_decrease()
        try:
            self.assertEqual(decount_modify, decount_show, msg="修改专项附加扣除出错")
        except Exception as e:
            print("Test Fail!", format(e))

    def test_5(self):
        """计算个税-工资薪金"""
        salary = 15000
        month = 5
        self.tax_page.open(self.url)
        self.tax_page.input_salary(salary)
        self.tax_page.select_month(month)
        sleep(0.5)
        fundcal = self.tax_page.get_fundcal()        
        self.tax_page.click_count()
        tax_result = self.result_page.result_salary(salary,fundcal,month)
        tax_onPage = self.result_page.get_result_tax()
        try:
            self.assertEqual(tax_onPage, tax_result, msg="个税计算结果有误")
        except Exception as e:
            print("Test Fail!", format(e))
        
    def test_6(self):
        """计算个税-年终奖"""
        bouns = 169980
        self.tax_page.open(self.url)
        self.tax_page.click_bouns()
        self.tax_page.input_bouns(bouns)
        self.tax_page.click_count()
        sleep(0.5)
        tax_result = self.result_page.result_bouns(bouns)
        tax_onpage = self.bounsTax_page.get_tax()
        # print(tax_result, tax_onpage)
        try:
            self.assertEqual(tax_onpage, tax_result, msg="个税计算错误")
        except Exception as e:
            print("Test Fail!", format(e))

    def test_7(self):
        """校验输入框"""
        self.tax_page.open(self.url)
        self.tax_page.input_salary(10000000000)
        flag = self.tax_page.toast_exist()
        try:
            if flag:
                pass
        except:
            raise Exception("Test Fail! 无Toast提示")
        
    def test_8(self):
        """专项附加扣除-同时勾选住房贷款和住房租金"""
        self.tax_page.open(self.url)
        self.tax_page.click_deItems()
        self.deItem_page.check_hosing_loan()
        self.deItem_page.check_hosing_rent() 
        flag = self.deItem_page.toast_exist()
        try:
            if flag:
                pass
        except:
            raise Exception("Test Fail! 无toast提示")


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    filename = now + '.html'

    suite = unittest.TestSuite()
    cases = [
        IncomeTax("test_1"),
        IncomeTax("test_2"),
        IncomeTax("test_3"),
        IncomeTax("test_4"),
        IncomeTax("test_5"),
        IncomeTax("test_6"),
        IncomeTax("test_7"),
        IncomeTax("test_8")
    ]

    suite.addTests(cases)
    runner = BeautifulReport(suite)
    runner.report(filename=filename, description="个税计算器测试报告", log_path="./report")

    # runner = unittest.TextTestRunner()
    # runner.run(suite)