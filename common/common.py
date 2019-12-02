import re
import xlrd
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

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
扬州：JSYZ-
'''
class BasePages(object):
    def __init__(self,selenium_driver,base_url):
        self.driver = selenium_driver
        self.base_url = base_url
        # self.pagetitle = pagetitle

    def on_page(self,pagetitle=None):
        return pagetitle in self.driver.title

    def _open(self,url,pagetitle=None):
        self.driver.get(url)
        self.driver.maximize_window()
        if pagetitle is not None:
            assert self.on_page(pagetitle),u"打开开页面失败 %s"%url

    # def open(self):
    #     # self._open(self.base_url,self.pagetitle)
    #     self._open(self.base_url)
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s页面 中未能找到%s元素"%(self , loc))

    def switch_frame(self,loc):
        return self.driver.switch_to_frame(loc)
    
    def script(self,src):
        self.driver.execute_script(src)

    # def send_keys(self, loc, value):
        # try:
        #     loc = getattr(self,"_%s"% loc)  #getattr相当于实现self.loc
        #     if click_first:
        #         self.find_element(*loc).click()
        #     if clear_first:
        #         self.find_element(*loc).clear()
        #         self.find_element(*loc).send_keys(vaule)
        # except AttributeError:
        #     print ("%s 页面中未能找到 %s 元素"%(self, loc))
    # 获取上下限
    def get_basecount_salary(self,driver,xpath,key):
        value = driver.find_element_by_xpath(xpath).get_attribute(key)
        # p = re.compile(r'[1-9]+\.?[0-9]*')
        # value = driver.find_element_by_xpath(xpath).get_attribute('placeholder')
        # value = driver.find_elements_by_xpath(xpath).get_attribute(key)
        p = p = re.compile(r'[1-9]+\.?[0-9]*')
        list1 = p.findall(value)
        return list1



    def get_data(self,filepath,sheetname):
        list = []
        workbook = xlrd.open_workbook(filepath)
        sheet = workbook.sheet_by_name(sheetname)
        lines = sheet.nrows
        clos = sheet.ncols
        for line in range(1,lines):
            for clo in range(0,clos):
                msg = {}
                msg['salary'] = sheet.cell_value(line, 0)
                msg['fund_percent'] = sheet.cell_value(line, 1)
                msg['fund_company'] = sheet.cell_value(line, 2)
                msg['supplement_percent'] = sheet.cell_value(line, 3)
            list.append(msg)
        return  list






