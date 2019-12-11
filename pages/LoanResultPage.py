from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
sys.path.append('C:\\code\\calculator')
from common.common import *
from time import sleep

class LoanResultPage(BasePages):

    # 等额本息tab
    loc_interest_tab = (By.XPATH, "//*[@id='payment_result']/div/div[1]/span[1]")
    # 等额本金tab
    Loc_capital_tab = (By.XPATH, "//*[@id='payment_result']/div/div[1]/span[2]")
    # 贷款总额显示框
    loc_total_loan = "//*[@id='payment_result']/div/div[3]/div[1]/span[2]"
    # 还款总额显示框
    loc_total_repay = "//*[@id='payment_result']/div/div[3]/div[2]/span[2]"
    # 支付利息显示框
    loc_interest_repay = "//*[@id='payment_result']/div/div[3]/div[3]/span[2]"

    def get_total_repay(self):
        """获取页面上还款总额"""
        total_repay = self.get_ele_value(self.driver, self.loc_total_repay, 'textContent')
        # value = self.get_num(total_repay)
        return float(total_repay[0])

    def get_total_interest(self):
        """获取页面上支付利息"""
        total_interest = self.get_ele_value(self.driver, self.loc_interest_repay, 'textContent')
        # value = self.get_num(total_interest)
        return float(total_interest[0])

    def select_tab_capital(self):
        """切换等额本金tab"""
        self.find_element(*self.Loc_capital_tab).click()