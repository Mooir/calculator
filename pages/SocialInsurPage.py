from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import BasePages

class SocialPage(BasePages):
    # URL
    base_url = "https://apps.eshiyun.info/tools/social?geoCode=SHS"
    # 税前收入输入框
    salary_input_loc = (By.XPATH,"//*[@id='social']/div[1]/div[2]/div[2]/div[2]/input")
    # 计算按钮
    count_loc = (By.CLASS_NAME,"social_btn")
    # 缴纳规则选择
    change_rule_loc = (By.XPATH, "//*[@id='social']/div[1]/div[2]/div[3]/div[1]/span[2]")
    # 缴纳规则-最低基数
    low_loc = (By.XPATH,"//*[@id='social']/div[1]/div[4]/div/div[2]/p[2]")
    # 缴纳规则-自定义基数
    customize_loc = (By.XPATH,"//*[@id='social']/div[1]/div[4]/div/div[2]/p[3]")
    # 缴纳规则选择-确定按钮
    confer_loc = (By.XPATH,"//*[@id='social']/div[1]/div[4]/div/div[1]/div[1]")
    # 社保基数输入框
    # cardinal_loc = (By.XPATH, "//*[@id='social']/div[1]/div[2]/div[3]/div[2]/input")
    cardinal_loc = "//*[@id='social']/div[1]/div[2]/div[3]/div[2]/input"


    def open(self):
        self._open(self.base_url)

    # 点击
    def click(self,loc):
        self.find_element(*loc).click()

    # 输入税前收入
    def input_salary(self, salary):
        self.find_element(*self.salary_input_loc).clear()
        self.find_element(*self.salary_input_loc).send_keys(salary)

    # 获取缴存基数下限
    def get_num_min(self):
        num = self.get_basecount_salary(self.driver, self.cardinal_loc, 'placeholder')
        return float(num[0])

    # 获取缴存基数上限
    def get_num_max(self):
        num = self.get_basecount_salary(self.driver, self.cardinal_loc, 'placeholder')
        return float(num[1])

    # 计算