import sys
sys.path.append('C:\\code\\calculator')
from selenium import webdriver
from selenium.webdriver.common.by import By
from common.common import *
from time import sleep


class ChCityPage(BasePages):

    loc_SH = "//*[@id='ChoiceCity']/div/div[2]/div[1]"
    loc_CS = "//*[@id='ChoiceCity']/div/div[2]/div[2]"
    loc_CD = "//*[@id='ChoiceCity']/div/div[2]/div[3]"
    loc_HK = "//*[@id='ChoiceCity']/div/div[3]/div[1]"
    loc_LZ = "//*[@id='ChoiceCity']/div/div[3]/div[2]"
    loc_ZMD = "//*[@id='ChoiceCity']/div/div[3]/div[3]"
    loc_YZ = "//*[@id='ChoiceCity']/div/div[4]/div"

    def select_city(self, city_code):
        if city_code == 'SH':
            self._find_ele('xpath', self.loc_SH).click()
        elif city_code == 'CS':
            self._find_ele('xpath', self.loc_CS).click()
        elif city_code == 'CD':
            self._find_ele('xpath', self.loc_CD).click()
        elif city_code == 'HK':
            self._find_ele('xpath', self.loc_HK).click()
        elif city_code == 'LZ':
            self._find_ele('xpath', self.loc_LZ).click()
        elif city_code == 'ZMD':
            self._find_ele('xpath', self.loc_ZMD).click()
        elif city_code == 'YZ':
            self._find_ele('xpath', self.loc_YZ).click()