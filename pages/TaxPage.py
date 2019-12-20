import sys
sys.path.append('C:\\code\\calculator')
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import *
from time import sleep


class TaxPage(BasePages):
    # 选择城市
    loc_choice_city = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[2]"
    loc_input_salary = "//*[@class='grey inputmonth']"
    # 选择月份
    loc_choice_month = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[7]"
    loc_month = "//*[@class='van-ellipsis van-picker-column__item']"
    loc_btn_confer = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[8]/div/div[1]/div[2]"
    