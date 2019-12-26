import sys
sys.path.append('./')
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import *
from time import sleep


"""
introduction：个税计算器主页
author：黄思梦
date-last-modified：2019-12-26
last-modified-by：黄思梦
"""

class TaxPage(BasePages):
    loc_year_bouns = "//*[@id='Tax2']/div[2]/div[1]/div[1]/div[2]"
    loc_input_bouns = "//*[@id='Tax2']/div[2]/div[1]/div[2]/input"
    # 选择城市
    loc_city = "//*[@id='Tax2']/div[2]/div[1]/div[2]/div[2]/input"
    loc_select_city = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[2]"
    loc_input_salary = "//*[@class='grey inputmonth']"
    loc_toast_input = "//div[@class='lx-toast lx-toast-center']"
    # 选择月份
    loc_month = "//input[@class='inputmonth']"
    loc_select_month = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[7]"
    loc_month_now = "//*[@class='van-ellipsis van-picker-column__item van-picker-column__item--selected']"
    loc_month_list = "//div[@class='van-picker-column']/ul/li"
    loc_btn_confer = "/html/body/div[1]/div/div[2]/div[1]/div[2]/div[8]/div/div[1]/div[2]"
    loc_modify_fundcal = "//*[@id='Tax2']/div[2]/div[1]/div[2]/div[13]"
    # 修改五险一金
    loc_fundcal = "//*[@id='Tax2']/div[2]/div[1]/div[2]/input[3]"
    loc_soci_insur = "//*[@id='definedSoc']"
    loc_fund_base = "//*[@id='definedFun']"
    loc_fund_percent = "//*[@id='per']"
    loc_fund_sup = "//*[@id='Tax2']/div[2]/div[1]/div[2]/div[16]/div[6]/input"
    
    # 专项附加扣除
    loc_decrease = "//*[@id='Tax2']/div[2]/div[1]/div[2]/div[20]"
    #专项附加扣除显示框
    loc_deItem_count = "//*[@id='Tax2']/div[2]/div[1]/div[2]/input[4]"

    loc_count = "//div[@class='calculate']"

    def open(self,url):
        self._open(url)

    def input_salary(self, salary):
        """输入本月工资收入"""
        el = self._find_ele('xpath', self.loc_input_salary)
        el.click()
        el.clear()
        el.send_keys(salary)

    def input_bouns(self, bouns):
        """输入年终奖"""
        el = self._find_ele('xpath', self.loc_input_bouns)
        el.send_keys(bouns)

    def click_bouns(self):
        self._find_ele('xpath', self.loc_year_bouns).click()

    def click_city(self):
        self._find_ele('xpath', self.loc_select_city).click()

    def click_deItems(self):
        self._find_ele('xpath', self.loc_decrease).click()

    def click_count(self):
        self._find_ele('xpath', self.loc_count).click()

    def get_city(self):
        """获取当前城市"""
        el = self._find_ele('xpath', self.loc_city)
        text = el.get_attribute('value')
        return text

    def get_month(self):
        """获取选择的月份"""
        el = self._find_ele('xpath', self.loc_month)
        month_text = el.get_attribute('value')
        return month_text

    def get_fundcal(self):
        """获取五险一金金额"""
        count = self._find_ele('xpath', self.loc_fundcal).get_attribute('value')
        return count

    def get_decrease(self):
        """获取专项附加扣除金额"""
        count = self._find_ele('xpath', self.loc_deItem_count).get_attribute('value')
        return count

    def select_month(self, month):
        """选择缴纳月数"""
        self._find_ele('xpath', self.loc_select_month).click()
        # 获取当前月份
        text = self._find_ele('xpath', self.loc_month_now).get_attribute('textContent')
        month_now = float((self.get_num(text))[0])
        month_now = int(month_now)-1
        month = month - 1
        month_list = self._find_ele('xpaths', self.loc_month_list)
        if month <= month_now:
            for month in range(month, month_now):
                month_now = month_now-1
                month_list[month_now].click()
                sleep(0.5)
        elif month > month_now:
            for month in range(month_now, month):
                month_now = month_now + 1
                month_list[month_now].click()
                sleep(0.5)
        self._find_ele('xpath', self.loc_btn_confer).click()

    def modify_fundcal(self, soc_insur, fund_base, fund_percent, per_fund_percent = None):
        city = self.get_city()
        self._find_ele('xpath', self.loc_modify_fundcal).click()
        # 获取社保基数上下限
        text_social = self._find_ele('xpath', self.loc_soci_insur).get_attribute('placeholder')
        list_social = self.get_num(text_social)
        soci_min = float(list_social[0])
        soci_max = float(list_social[1])
        # print(soci_max, soci_min)

        # 获取公积金缴纳基数
        text_fund = self._find_ele('xpath', self.loc_fund_base).get_attribute('placeholder')
        list_fund = self.get_num(text_fund)
        fund_min = float(list_fund[0])
        fund_max = float(list_fund[1])
        # print(fund_max, fund_min)

        # 获取公积金缴纳比例
        per1 = self._find_ele('xpath', self.loc_fund_percent).get_attribute('value')
        per2 = self._find_ele('xpath', self.loc_fund_sup).get_attribute('value')
        fund_per = float(per1)
        fund_per_sup = float(per2)
        # print(fund_per, fund_per_sup)

        self._find_ele('xpath', self.loc_soci_insur).send_keys(soc_insur)
        self._find_ele('xpath', self.loc_fund_base).send_keys(fund_base)
        self._find_ele('xpath', self.loc_fund_percent).send_keys(fund_percent)
        if city == '上海':
            self._find_ele('xpath', self.loc_fund_sup).send_keys(per_fund_percent)
            self._find_ele('xpath', self.loc_input_salary).click()
        else:
            self._find_ele('xpath', self.loc_input_salary).click()
        # 修改后的五险一金
        new = self.get_fundcal()
        return new

    def toast_exist(self):
        flag = True
        try:
            self._find_ele('xpath', self.loc_toast_input)
            return flag
        except:
            flag = False
            return flag
            





