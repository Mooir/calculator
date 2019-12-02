from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import BasePages

class SocialResult(BasePages):
    # 合计
    total_count_loc = "//*[@id='social_result']/div/div[2]/p[1]"
    # 单位缴纳
    company_count_loc = "//*[@id='social_result']/div/div[3]/div[1]/p[1]"
    # 个人缴纳
    personal_count_loc = "//*[@id='social_result']/div/div[3]/div[2]/p[1]"
    # 单位缴纳各项比例：
    percent_company_locs = "//div[@class='social_table']/div/p[2]/span"
    # 个人缴纳各项比例：
    percent_personal_locs = "//div[@class='social_table']/div/p[3]/span"

    # 获取比例


