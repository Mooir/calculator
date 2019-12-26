import sys
sys.path.append('./')
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import *
from time import sleep

"""
introduction：个税计算器：薪资计算结果页
author：黄思梦
date-last-modified：2019-12-26
last-modified-by：黄思梦
"""


class RSalaryPage(BasePages):
    loc_result_tax = "//*[@id='tax_result']/div[2]/div[21]"

    def get_result_tax(self):
        """获取页面上的个税结果"""
        tax_text = self._find_ele('xpath', self.loc_result_tax).get_attribute('textContent')
        return float(tax_text)

    def result_salary(self, salary, fundcal, month, decrease = 0):
        """根据税前月薪，五险一金，附加扣除计算每月个税"""
        salary = float(salary)
        fundcal = float(fundcal)
        month = int(float(month))
        decrease = float(decrease)

        temp = salary-fundcal-5000-decrease
        # print(temp)
        month_tax = []
        count = 0
        for i in range(1, 13):
            """计算每个月个税"""
            k = temp * i
            # print(k)
            if 0 < k <= 36000:
                rate_tax = 0.03
                part_tax = 0
            elif 36000 < k <= 144000:
                rate_tax = 0.1
                part_tax = 2520
            elif 144000 < k <= 300000:
                rate_tax = 0.2
                part_tax = 16920
            elif 300000 < k <= 420000:
                rate_tax = 0.25
                part_tax = 31920
            elif 420000 < k <= 660000:
                rate_tax = 0.3
                part_tax = 52920
            elif 660000 < k <= 960000:
                rate_tax = 0.35
                part_tax = 85920
            elif k > 960000:
                rate_tax = 0.45
                part_tax = 181920
            month_tax.append(k * rate_tax - part_tax - count)
            count = month_tax[i - 1] + count
        return month_tax[month-1]

    def result_bouns(self, bouns):
        """计算年终奖个税"""
        month_bouns = bouns/12
        if 0 < month_bouns <= 300:
            rate_tax = 0.03
            part_tax = 0
        elif 3000 < month_bouns <= 12000:
            rate_tax = 0.1
            part_tax = 210
        elif 12000 < month_bouns <= 25000:
            rate_tax = 0.2
            part_tax = 1410
        elif 25000 < month_bouns <= 35000:
            rate_tax = 0.25
            part_tax = 2660
        elif 35000 < month_bouns <= 55000:
            rate_tax = 0.3
            part_tax = 4410
        elif 55000 < month_bouns <= 80000:
            rate_tax = 0.35
            part_tax = 7160
        elif month_bouns > 960000:
            rate_tax = 0.45
            part_tax = 15160
        tax = bouns * rate_tax - part_tax
        return tax
