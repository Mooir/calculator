from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import *
from time import sleep

class LoanPage(BasePages):
    base_url = "https://apps.eshiyun.info/tools/"
    # 公积金贷款tab
    loc_acc_loan = (By.XPATH, "//*[@id='repay']/div[1]/div[1]/ul/li[1]")
    # 商业贷款tab
    loc_buss_loan = (By.XPATH, "//*[@id='repay']/div[1]/div[1]/ul/li[2]")
    # 组合贷款tab
    loc_mix_loan = (By.XPATH, "//*[@id='repay']/div[1]/div[1]/ul/li[3]")
    # 公积金贷款金额输入框
    loc_input_acc = (By.ID, "loan_sum")
    # 商业贷款金额输入框
    loc_input_buss = (By.ID, "business_sum")
    # 贷款年限显示框
    loc_year = (By.XPATH, "//*[@id'year_id']")
    
