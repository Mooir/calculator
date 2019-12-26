import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import BasePages
from pages.SocialInsurPage import *


"""
introduction：社保计算器计算结果页
author：黄思梦
date-last-modified：2019-12-26
last-modified-by：黄思梦
"""


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
    # insurance_page = SocialPage()

    # 获取比例[[x],[x],[x]]形式
    def _get_percent_part1(self, xpath):
        texts = self.driver.find_elements_by_xpath(xpath)
        lists = []
        nums = []
        for text in texts:
            value1 = text.text
            lists.append(value1)
            for list_value in lists:
                value2 = BasePages.get_num(self, list_value)
            nums.append(value2)
            if [] in nums:
                nums.remove([])
        return nums

    # 获取比例[x,x,x,x]形式
    def _get_percent_part2(self, xpath):
        num = []
        nums = self._get_percent_part1(xpath)
        for i in range(0, len(nums)):
            num1 = float(nums[i][0])
            num.append(num1)
        return num

    # 比例求和
    def _get_total_percent(self, xpath):
        num = 0.0
        nums  = self._get_percent_part2(xpath)
        for i in nums:
            num = num+i
        return num/100

    # 单位比例之和
    def _get_total_company(self):
        total_percent_company = self._get_total_percent(self.percent_company_locs)
        return total_percent_company

    # 个人缴纳比例之和
    def _get_total_personal(self):
        total_percent_personal = self._get_total_percent(self.percent_personal_locs)
        return total_percent_personal

    # 自定义计算结果-自定义基数/税前工资
    def get_result(self, base_soc_fund, min, max):
        if float(base_soc_fund) < min:
            base_soc_fund = min
        elif float(base_soc_fund) > max:
            base_soc_fund = max
        elif min <= float(base_soc_fund) <= max:
            base_soc_fund = float(base_soc_fund)
        count_comp = base_soc_fund*self._get_total_company()
        count_pers = base_soc_fund*self._get_total_personal()
        count = round(count_comp,2) + round(count_pers,2)
        # return math.floor(count*10**1)/(10**1)
        return math.floor(count)

    # 自定义计算结果-按最低基数缴纳
    def get_result_lowest(self, min):
        count_comp = min*self._get_total_company()
        count_pers = min*self._get_total_personal()
        count = round(count_comp,2) + round(count_pers,2)
        # return math.floor(count*10**1)/(10**1)
        return math.floor(count)
        
    # 获取页面上计算结果
    def get_pageResult(self):
        text = self.get_ele_value(self.driver, self.total_count_loc, 'textContent')
        # return math.floor(float(text[0])*10**1)/(10**1)
        return math.floor(float(text[0]))
