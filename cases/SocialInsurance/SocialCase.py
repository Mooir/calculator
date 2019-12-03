import re
import unittest
from time import sleep
from pages.SocialInsurPage import *
from pages.SocialResultPage import *

class SocialCount(unittest.TestCase):
    def setUp(self):
        mobile_emulation = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(30)
        self.url = "https://apps.eshiyun.info/tools/social?geoCode=SHS"
        self.social_page = SocialPage(self.driver,self.url)
        self.result_page = SocialResult(self.driver, self.url)
        self.salary = 10000.73
        self.base_soc_fund=10000.71

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        self.social_page.open()
        sleep(0.5)
        self.social_page.click(self.social_page.change_rule_loc)
        sleep(0.5)
        self.social_page.click(self.social_page.customize_loc)
        self.social_page.click(self.social_page.confer_loc)
        sleep(1)
        min = self.social_page.get_num_min()
        max = self.social_page.get_num_max()
        print("缴存基数上下限分别为：", max, min)
        # print("缴存基数上限为：", max)
        self.social_page.input_salary(str(self.salary))
        self.social_page.input_soc_fund(str(self.base_soc_fund))
        self.social_page.click(self.social_page.count_loc)
        sleep(1)
        val1 = self.result_page.get_result(self.base_soc_fund, min, max)
        print("实际结果应为：",val1)
        val2 = self.result_page.get_pageResult()
        print("页面上结果为：",val2)
        print("-----------------------------------------")
        try:
            self.assertEqual(val1, val2, "自定义社保基数-计算结果错误！")
        except Exception as e:
            print("Test Fail!",format(e))
        sleep(10)
        self.driver.back()





if __name__ == "__main__":
    unittest.main()