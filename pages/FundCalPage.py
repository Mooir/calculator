import sys
sys.path.append('C:\\code\\calculator')
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import BasePages

class FundCalPage(BasePages):
    salary_loc = (By.ID,'salary')
    fund_percent_loc = (By.ID,'fund_percent')
    fund_company_loc = (By.ID,'fund_company')
    supplement_percent_loc = (By.ID,'supplement_percent')
    count_loc = (By.CLASS_NAME,'repay_btn')
    per_fund_loc = (By.XPATH,"//*[@id='payment']/div[1]/div[4]/div/div[1]/div/input")
    per_supfund_loc = (By.XPATH,"//*[@id='payment']/div[1]/div[4]/div/div[2]/div/input")
    # 有补充公积金
    total_loc1 = "//*[@id='payment']/div[1]/div[4]/div/div[3]/div/input"
    # 无补充公积金
    total_loc2 = "//*[@id='payment']/div[1]/div[4]/div/div[1]/div/input"
    text_xpath = "//*[@id='payment']/div[1]/div[3]/p"
    # 测试用例表格
    filepath = "C:/code/calculator/cases/FundCalculator/testcase.xlsx"
    sheetname_SH = "Sheet1"
    sheetname_other = "Sheet2"
    base_url = "https://apps.eshiyun.info/tools/gjjPayment?geoCode=SHS"

    def open(self):
        self._open(self.base_url)

    # 输入工资
    def input_salary(self,salary):
        self.find_element(*self.salary_loc).clear()
        self.find_element(*self.salary_loc).send_keys(salary)

    # 输入个人公积金缴存比例
    def input_fund_percent(self,fund_percent):
        self.find_element(*self.fund_percent_loc).clear()
        self.find_element(*self.fund_percent_loc).send_keys(fund_percent)

    # 输入公司公积金缴存比例
    def input_fund_company(self,fund_company):
        self.find_element(*self.fund_company_loc).clear()
        self.find_element(*self.fund_company_loc).send_keys(fund_company)

    # 输入补充公积金缴存比例
    def input_sup_percent(self,sup_percent):
        self.find_element(*self.supplement_percent_loc).clear()
        self.find_element(*self.supplement_percent_loc).send_keys(sup_percent)

    # 点击计算
    def click_count(self):
        self.find_element(*self.count_loc).click()

    # 获取缴存基数上限
    def get_max_salary(self):
        max = self.get_ele_value(self.driver,self.text_xpath, 'textContent')
        return float(max[2])

    # 获取缴存基数下限
    def get_min_salary(self):
        min = self.get_ele_value(self.driver, self.text_xpath, 'textContent')
        return float(min[3])

    # 上海： 自定义计算-公积金
    def count(self, salary, fund_percent, fund_company, sup_percent):
        if float(fund_percent) < 5:
            fund_percent = 5
        if float(fund_percent) > 7:
            fund_percent = 7
        if float(fund_company) < 5:
            fund_company = 5
        if float(fund_company) > 7:
            fund_company = 7
        if float(sup_percent) > 5:
            sup_percent = 5
        if float(sup_percent) < 1:
            sup_percent = 1
        total = (float(fund_company) + float(fund_percent) + float(sup_percent))/100
        if self.get_min_salary() <= float(salary) <= self.get_max_salary():
            count_total = float(salary)*total
        elif float(salary) < self.get_min_salary():
            count_total = self.get_min_salary()*total
        elif float(salary) > self.get_max_salary():
            count_total = self.get_max_salary()*total
        return round(count_total,2)

    # 其他城市：自定义计算-公积金
    def count_other(self, salary, fund_percent, fund_company):
        if float(fund_percent) < 5:
            fund_percent = 5
        if float(fund_percent) > 12:
            fund_percent = 12
        if float(fund_company) < 5:
            fund_company = 5
        if float(fund_company) > 12:
            fund_company = 12
        total = (float(fund_company) + float(fund_percent))/100
        if self.get_min_salary() <= float(salary) <= self.get_max_salary():
            count_total = float(salary)*total
        elif float(salary) < self.get_min_salary():
            count_total = self.get_min_salary()*total
        elif float(salary) > self.get_max_salary():
            count_total = self.get_max_salary()*total
        return round(count_total,2)

    # 获取测试用例数据--上海
    def get_SH_testdata(self):
        list = self.get_data(self.filepath, self.sheetname_SH)
        return list

    # 获取测试用例--其他城市
    def get_other_testdata(self):
        list = self.get_data(self.filepath, self.sheetname_other)
        return list