
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import BasePages

class FundCalPage(BasePages):
    # driver = webdriver.Chrome()
    salary_loc = (By.ID,'salary')
    fund_percent_loc = (By.ID,'fund_percent')
    fund_company_loc = (By.ID,'fund_company')
    supplement_percent_loc = (By.ID,'supplement_percent')
    count_loc = (By.CLASS_NAME,'repay_btn')
    per_fund_loc = (By.XPATH,"//*[@id='payment']/div[1]/div[4]/div/div[1]/div/input")
    per_supfund_loc = (By.XPATH,"//*[@id='payment']/div[1]/div[4]/div/div[2]/div/input")
    # 有补充公积金
    total_loc1 = "//*[@id='payment']/div[1]/div[4]/div/div[3]/div/input"
    # total_loc1 = (By.XPATH,"//*[@id='payment']/div[1]/div[4]/div/div[3]/div/input")
    # 无补充公积金//*[@id="payment"]/div[1]/div[4]/div/div[1]/div/input
    # total_loc2 = (By.XPATH,"//*[@id='payment']/div[1]/div[4]/div/div[1]/div/input")
    # total_loc2 = "//*[@id='payment']/div[1]/div[4]/div/div[3]/div/input"
    total_loc2 = "//*[@id='payment']/div[1]/div[4]/div/div[1]/div/input"
    text_xpath = "//*[@id='payment']/div[1]/div[3]/p"


    def open(self):
        self._open(self.base_url,self.pagetitle)

    # 输入工资
    def input_salary(self,salary):
        self.find_element(*self.salary_loc).send_keys(salary)

    # 输入个人公积金缴存比例
    def input_fund_percent(self,fund_percent):
        self.find_element(*self.fund_percent_loc).send_keys(fund_percent)

    # 输入公司公积金缴存比例
    def input_fund_company(self,fund_company):
        self.find_element(*self.fund_company_loc).send_keys(fund_company)

    # 输入补充公积金缴存比例
    def input_sup_percent(self,sup_percent):
        self.find_element(*self.supplement_percent_loc).send_keys(sup_percent)

    # 点击计算
    def click_count(self):
        self.find_element(*self.count_loc).click()

    # 获取缴存基数上限
    def get_max_salary(self):
        max = self.get_basecount_salary(self.driver,self.text_xpath)
        return float(max[2])

        # 获取缴存基数下限
    def get_min_salary(self):
        min = self.get_basecount_salary(self.driver, self.text_xpath)
        return float(min[3])

    # 自定义计算-公积金
    def count(self,salary,fund_percent,fund_company,sup_percent):
        if self.is_supfund_exists():
            total = (fund_percent + fund_company + sup_percent)/100
            count_total = round(salary*total, 2)
        else:
            total = (fund_percent + fund_company + 0) / 100
            count_total = round(salary*total, 2)
        return count_total