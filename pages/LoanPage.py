import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import *
from time import sleep

class LoanPage(BasePages):
    base_url = "https://apps.eshiyun.info/tools/"
    # 公积金贷款tab
    loc_acc_tab = (By.XPATH, "//*[@id='repay']/div[1]/div[1]/ul/li[1]")
    # 商业贷款tab
    loc_buss_tab = (By.XPATH, "//*[@id='repay']/div[1]/div[1]/ul/li[2]")
    # 组合贷款tab
    loc_mix_tab = (By.XPATH, "//*[@id='repay']/div[1]/div[1]/ul/li[3]")
    # 公积金贷款金额输入框
    loc_input_acc = (By.ID, "loan_sum")
    # 商业贷款金额输入框
    loc_input_buss = (By.ID, "business_sum")
    # 贷款年限显示框
    loc_year = "//input[@id='year_id']"
    # 公积金贷款利率显示框
    loc_acc_rate = "//*[@id='interest_id']"
    # 商贷利率显示框
    loc_buss_rate = "//*[@id='busi_interest_id']"
    # 还款方式-等额本息
    loc_interest = (By.XPATH, "//*[@id='tabContent']/div[1]/div[6]/div/span[1]")
    # 还款方式-等额本金
    loc_principal = (By.XPATH, "//*[@id='tabContent']/div[1]/div[6]/div/span[2]")
    # 开始计算按钮
    loc_count = (By.XPATH, "//*[@id='repay']/div[1]/div[3]/a")
    # 贷款年限&利率
    loc_select = "//li[@class='wheel-item']"
    # 选择栏确认按钮
    loc_confer = "//span[@class='pt-submit']"

    # 打开贷款计算器
    def open(self):
        self._open(self.base_url)

    # 产生随机数
    def randit(self, val1,val2):
        return random.randint(val1, val2)

    # 获取贷款年限文本框内容
    def get_value_year(self):
        list = self.get_ele_value(self.driver, self.loc_year , 'value')
        return int(list[0])

    # 获取公积金贷款利率
    def get_acc_rate(self):
        list = self.get_ele_value(self.driver, self.loc_acc_rate, 'value')
        return float(list[0])

    # 获取商贷利率
    def get_buss_rate(self):
        list = self.get_ele_value(self.driver, self.loc_buss_rate, 'value')
        return float(list[0])

    # 选择贷款年限
    def select_year(self, year_num):
        # self.find_element(*self.loc_year).click()
        self.driver.find_element_by_xpath(self.loc_year).click()
        sleep(0.5)
        list = self.driver.find_elements_by_xpath(self.loc_select)
        for i in range(0, 31-year_num):
            list[i].click()
            sleep(0.5)
        sleep(0.5)
        self.driver.find_elements_by_xpath(self.loc_confer)[0].click()