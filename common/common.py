from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
from time import sleep

# 贷款：
# https://apps.eshiyun.info/tools/ 
#
# # 个税：
# https://apps.eshiyun.info/tools/tax2?geoCode=HNZMD 
#
# # 公积金：
# https://apps.eshiyun.info/tools/gjjPayment?geoCode=HNZMD
#
# # 社保：
# https://apps.eshiyun.info/tools/social?geoCode=HNZMD

# 城市代码
'''
上海：SHS--有补充公积金
长沙：HNCS
成都：SCCD
海口：HNHK
柳州：GXLZ
驻马店：HNZMD
扬州：JSYZ
'''
class BasePages(object):
    def __init__(self,selenium_driver,base_url,pagetitle):
        self.driver = selenium_driver
        self.base_url = base_url
        self.pagetitle = pagetitle

    def on_page(self,pagetitle):
        return pagetitle in self.driver.title

    def _open(self,url,pagetitle):
        self.driver.get(url)
        self.driver.maximize_window()
        assert self.on_page(pagetitle),u"打开开页面失败 %s"%url

    def open(self):
        self._open(self.base_url,self.pagetitle)

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s页面 中未能找到%s元素"%(self,loc))

    def switch_frame(self,loc):
        return self.driver.switch_to_frame(loc)
    
    def script(self,src):
        self.driver.execute_script(src)

    def send_keys(self, loc, vaule, clear_first=True, click_first=True):
        try:
            loc = getattr(self,"_%s"% loc)  #getattr相当于实现self.loc
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(vaule)
        except AttributeError:
            print ("%s 页面中未能找到 %s 元素"%(self, loc))
