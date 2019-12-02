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

    def tearDown(self):
        self.driver.quit()

    def test_1(self):
        self.social_page.open()
        sleep(2)
        # self.social_page.click(self.social_page.change_rule_loc)
        # sleep(0.5)
        # self.social_page.click(self.social_page.customize_loc)
        # self.social_page.click(self.social_page.confer_loc)
        # sleep(1)
        # print(self.social_page.get_num_min())
        # print(self.social_page.get_num_max())


        self.social_page.input_salary(10000)
        self.social_page.click(self.social_page.count_loc)
        sleep(1)
        texts = self.driver.find_elements_by_xpath(self.result_page.percent_company_locs)
        for text in texts:
            print(text.text)




if __name__ == "__main__":
    unittest.main()