import re
import xlrd
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

    def get_ele(self, type, value):
        if type == 'id':
            el = self.driver.find_element_by_id(value)
        elif type == "name":
            el = self.driver.find_element_by_name(value)
        elif type == "class_name":
            el = self.driver.find_element_by_class_name(value)
        elif type == "tag_name":
            el = self.driver.find_element_by_tag_name(value)
        elif type == "link_text":
            el = self.driver.find_element_by_link_text(value)
        elif type == "partial_link_text":
            el = self.driver.find_element_by_partial_link_text(value)
        elif type == "xpath":
            el = self.driver.find_element_by_xpath(value)
        elif type == "css_selector":
            el = self.driver.find_element_by_css_selector(value)
        elif type == "class_names":
            el = self.driver.find_elements_by_class_name(value)
        elif type == "xpaths":
            el = self.driver.find_elements_by_xpath(value)
        return el

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

    def get_basecount_salary(self,driver,xpath):
        value = driver.find_element_by_xpath(xpath).get_attribute('textContent')
        p = re.compile(r'[1-9]+\.?[0-9]*')
        list1 = p.findall(value)
        return list1

    def get_data(self,filepath,sheetname):
        list = []
        workbook = xlrd.open_workbook(filepath)
        # workbook = xlrd.open_workbook(u"C:/code/calculator/cases/testcase.xlsx")
        sheet = workbook.sheet_by_name(sheetname)
        lines = sheet.nrows
        clos = sheet.ncols
        for line in range(1,lines):
            for clo in range(0,clos):
                msg = {}
                msg['salary'] = int(sheet.cell_value(line,clo))
                msg['fund_percent'] = int(sheet.cell_value(line, clo))
                msg['fund_company'] = int(sheet.cell_value(line, clo))
                msg['sup_fund'] = int(sheet.cell_value(line, clo))
                return msg
            list.append(self.msg)
        return  list






