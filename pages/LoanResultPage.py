from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import *
from time import sleep

class LoanResultPage(BasePages):

    # 等额本息tab
    loc_interest_tab = (By.XPATH, "//*[@id='payment_result']/div/div[1]/span[1]")
    # 等额本金tab
    loc_principal_tab = (By.XPATH, "//*[@id='payment_result']/div/div[1]/span[2]")
    # 贷款总额显示框
    loc_total_loan = "//*[@id='payment_result']/div/div[3]/div[1]/span[2]"
    # 还款总额显示框
    loc_total_repay = "//*[@id='payment_result']/div/div[3]/div[2]/span[2]"
    # 支付利息显示框
    loc_rate_repay = "//*[@id='payment_result']/div/div[3]/div[3]/span[2]"
