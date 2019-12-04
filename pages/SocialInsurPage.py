from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import *
from time import sleep

class SocialPage(BasePages):
    # URL
    base_url = "https://apps.eshiyun.info/tools/social?geoCode=SHS"
    # 税前收入输入框
    salary_input_loc = (By.XPATH,"//*[@id='social']/div[1]/div[2]/div[2]/div[2]/input")
    # 自定义社保基数输入框
    cardinal_loc1 = (By.XPATH, "//*[@id='social']/div[1]/div[2]/div[3]/div[2]/input")
    cardinal_loc = "//*[@id='social']/div[1]/div[2]/div[3]/div[2]/input"
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
    # toast提示
    toast_info_loc = (By.CLASS_NAME, "lx-toast lx-toast-center")
    # 测试用例数据：
    filepath = "C:/code/calculator/cases/SocialInsurance/TestData.xlsx"
    # 表名--自定义社保基数
    sheetname_cardinal_Y = "Sheet1"
    sheetname_cardinal_N = "Sheet2"



    def open(self):
        self._open(self.base_url)

    # 点击
    def click(self,loc):
        self.find_element(*loc).click()

    # 输入税前收入
    def input_salary(self, salary):
        self.find_element(*self.salary_input_loc).clear()
        self.find_element(*self.salary_input_loc).send_keys(salary)

    # 输入自定义社保基数
    def input_soc_fund(self, soc_fund):
        self.find_element(*self.cardinal_loc1).clear()
        self.find_element(*self.cardinal_loc1).send_keys(soc_fund)

    # 选择社保缴纳规则-自定义基数缴纳
    def rule_cardinal(self):
        self.click(self.change_rule_loc)
        sleep(0.5)
        self.click(self.customize_loc)
        self.click(self.confer_loc)


    # 获取缴存基数下限
    def get_num_min(self):
        num = self.get_ele_value(self.driver, self.cardinal_loc, 'placeholder')
        return float(num[0])

    # 获取缴存基数上限
    def get_num_max(self):
        num = self.get_ele_value(self.driver, self.cardinal_loc, 'placeholder')
        return float(num[1])

    # 获取自定义社保基数测试数据-正常情况
    def get_cardinal_dataY(self):
        list = self.read_excel(self.filepath, self.sheetname_cardinal_Y)
        return list

    # 获取自定义社保基数测试数据-非正常情况（有toast提示）
    def get_cardinal_dataN(self):
        list = self.read_excel(self.filepath, self.sheetname_cardinal_N)
        return list

    def find_toast(self):
        text = self.get_ele_value(self.driver,self.toast_info_loc,'contentText')
        return text