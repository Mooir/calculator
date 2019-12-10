import random
import sys
import math
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
sys.path.append('C:\\code\\calculator')
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
    # 测试数据
    filepath = "C:/code/calculator/cases/loan/TestData.xlsx"
    sheetname_acc = "Sheet1"
    sheetname_buss = "Sheet2"
    sheetname_mix = "Sheet3"

    # 打开贷款计算器
    def open(self):
        self._open(self.base_url)

    # 产生随机数
    def randit(self, int1,int2):
        return random.randint(int1, int2)

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

    # 输入贷款公积金金额
    def input_acc_count(self, keys):
        self.find_element(*self.loc_input_acc).clear()
        self.find_element(*self.loc_input_acc).send_keys(keys)

    # 输入商业贷款金额
    def input_buss_count(self, keys):
        self.find_element(*self.loc_input_buss).clear()
        self.find_element(*self.loc_input_buss).send_keys(keys)

    # 点击计算
    def click_count(self):
        self.find_element(*self.loc_count).click()

    # 选择贷款年限[0-29]
    def select_year(self, year_num):
        year_num = int(float(year_num))
        # self.find_element(*self.loc_year).click()
        self.driver.find_element_by_xpath(self.loc_year).click()
        sleep(0.2)
        list = self.driver.find_elements_by_xpath(self.loc_select)
        for i in range(0, 31-year_num):
            list[i].click()
            sleep(0.5)
        # sleep(0.5)
        self.driver.find_elements_by_xpath(self.loc_confer)[0].click()

    # 选择公积金贷款利率[30-31]
    def select_acc_rate(self):
        self.driver.find_element_by_xpath(self.loc_acc_rate).click()
        sleep(0.5)
        list = self.driver.find_elements_by_xpath(self.loc_select)
        acc_rate = self.randit(30, 31)
        list[acc_rate].click
        self.driver.find_elements_by_xpath(self.loc_confer)[1].click()

    # 选择商业贷款利率[32-47]
    def select_buss_rate(self):
        self.driver.find_element_by_xpath(self.loc_buss_rate).click()
        sleep(0.5)
        list = self.driver.find_elements_by_xpath(self.loc_select)
        buss_rate = self.randit(32, 47)
        for i in range(32, buss_rate):
            list[i].click
            sleep(0.5)
        self.driver.find_elements_by_xpath(self.loc_confer)[2].click()

    # 获取公积金贷款测试数据
    def get_acc_testdata(self):
        list = self.read_excel(self.filepath, self.sheetname_acc)
        return list
    
    # 获取商业贷款测试数据
    def get_buss_testdata(self):
        list = self.read_excel(self.filepath, self.sheetname_buss)
        return list

    def get_mix_testdata(self):
        """获取组合贷款测试数据"""
        list = self.read_excel(self.filepath, self.sheetname_mix)
        return list

    def repay_equal_capital(self, capital, y_rate, periods):
        """等额本金"""
        count = 0
        periods = 12*periods
        for i in range(0, periods):

        monthlyPayment[i] = np.around(
            (mortgage/month)+
            (
                (mortgage)*monthlyInterestRate(anualInterestRate)
            ) - 
            (i*(mortgage/month)*monthlyInterestRate(anualInterestRate)),2)



            m_capital = capital/periods             #每月应还本金

            m_repay[i] = np.round((capital/periods)+((capital)))
        return

    def _month_rate(self, y_rate):
        """每月利率"""
        return (y_rate/12)/100

    def _total_rate(self, capital, m_repay, periods)
        """总利息"""
        return m_repay*(periosd*12) - capital

    def _equal_capital_rate(self, periods):
        """比例系数-每月应还"""
        R = self._month_rate
        N = periods*12
        I = R * math.pow(1+R, N)/ (math.pow(1+R, N)-1)
        return I




