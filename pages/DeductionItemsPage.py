import random
import sys
sys.path.append('./')
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import *
from time import sleep


class DeItemPage(BasePages):
    loc_decrease = "//*[@id='app']/div/div[1]/div[2]"
    # 子女教育
    loc_chedu_off = "//*[@id='app']/div/div[2]/div[1]/img[1]"
    # loc_chedu_on = "//*[@id='app']/div/div[2]/div[1]/img[2]"
    loc_child_count = "//*[@id='app']/div/div[2]/div[1]/div[4]/input[1]"
    loc_child_add = "//*[@id='app']/div/div[2]/div[1]/div[4]/div[6]"
    loc_child_dec = "//*[@id='app']/div/div[2]/div[1]/div[4]/div[4]"
    

    # 继续教育
    loc_educonti_off = "//*[@id='app']/div/div[2]/div[2]/img[1]"
    # loc_educonti_on = "//*[@id='app']/div/div[2]/div[2]/img[2]"
    loc_edu_vocation = "//*[@id='app']/div/div[2]/div[2]/div[5]/img[3]"

    # 住房贷款和住房租金只能勾选一个
    # 住房贷款
    loc_thousand = "//*[@id='app']/div/div[2]/div[3]/div[5]/img[1]"
    loc_hundred = "//*[@id='app']/div/div[2]/div[3]/div[5]/img[3]"
    # 住房租金
    loc_rent = "//*[@id='app']/div/div[2]/div[4]/img[1]"
    loc_toast = "//div[@class='lx-toast lx-toast-center']"

    # 赡养老人
    loc_support_oldest = "//*[@id='app']/div/div[2]/div[5]/img[1]"
    loc_count_add = "//*[@id='app']/div/div[2]/div[5]/div[4]/div/div[2]/div[3]"
    loc_count_dec = "//*[@id='app']/div/div[2]/div[5]/div[4]/div/div[2]/div[1]"

    loc_btn_save = "//*[@id='app']/div/div[2]/div[7]"


    def check_child_edu(self):
        """子女教育"""
        self._find_ele('xpath', self.loc_chedu_off).click()

    def check_continue_edu(self):
        """继续教育"""
        self._find_ele('xpath', self.loc_educonti_off).click()

    def check_hosing_loan(self):
        """住房贷款-和住房租金不可同时选中"""
        flag = random.randint(0,1)
        if flag == 0:
            self._find_ele('xpath', self.loc_thousand).click()
        else:
            self._find_ele('xpath', self.loc_hundred).click()

    def check_hosing_rent(self):
        """住房租金-和住房贷款不可同时选中"""
        self._find_ele('xpath', self.loc_rent).click()

    def check_provide_oldest(self):
        """赡养老人"""
        self._find_ele('xpath', self.loc_support_oldest).click()

    def click_save(self):
        self.slither_end()
        self._find_ele('xpath', self.loc_btn_save).click()

    def get_total_decrease(self):
        """获取附加扣除总额"""
        self.slither_top()
        text = self._find_ele('xpath', self.loc_decrease).get_attribute('textContent')
        list_text = self.get_num(text)
        return list_text[0]

    def toast_exist(self):
        """toast信息是否存在"""
        flag = True
        try:
            self._find_ele('xpath', self.loc_toast)
            return flag
        except:
            flag = False
            return flag