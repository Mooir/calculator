import re
import xlrd
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

# 贷款：
# https://apps.eshiyun.info/tools/ 
#
# # 个税：
# https://apps.eshiyun.info/tools/tax2?geoCode=HNZMD 
#
# # 公积金-完成：
# https://apps.eshiyun.info/tools/gjjPayment?geoCode=HNZMD
#
# # 社保-完成：
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

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s页面 中未能找到%s元素"%(self, *loc))

    def _find_ele(self, type, value):
        """定位元素"""
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

    def switch_frame(self, *loc):
        return self.driver.switch_to_frame(*loc)
    
    def script(self,src):
        self.driver.execute_script(src)

    def get_ele_value(self, driver, xpath, key):
        """获取元素的内容"""
        value = driver.find_element_by_xpath(xpath).get_attribute(key)
        list_limits = self.get_num(value)
        return list_limits

    def get_num(self, str):
        """提取文本中的数字"""
        p = re.compile(r'[0-9]+\.?[0-9]*')
        # p = re.compile(r'\d +.?\d *')
        list_num = p.findall(str)
        return list_num

    def get_data(self, filepath, sheetname):
        list = []
        workbook = xlrd.open_workbook(filepath)
        sheet = workbook.sheet_by_name(sheetname)
        lines = sheet.nrows
        clos = sheet.ncols
        for line in range(1, lines):
            for clo in range(0, clos):
                msg = {}
                msg['salary'] = sheet.cell_value(line, 0)
                msg['fund_percent'] = sheet.cell_value(line, 1)
                msg['fund_company'] = sheet.cell_value(line, 2)
                msg['supplement_percent'] = sheet.cell_value(line, 3)
            list.append(msg)
        return  list

    def read_excel(self, filepath, sheetname):
        data = xlrd.open_workbook(filepath)
        table = data.sheet_by_name(sheetname)
        keys = table.row_values(0)
        rowNum = table.nrows
        colNum = table.ncols
        if rowNum < 2:
            print("表格内数据行数小于2行")
        else:
            L = []
            for i in range(1, rowNum):
                sheet_data = {}
                for j in range(colNum):
                    sheet_data[keys[j]] = table.row_values(i)[j]
                L.append(sheet_data)
            return L

    def slither_end(self):
        js = "var str=document.documentElement.scrollTop=1000000"
        self.driver.execute_script(js)
        sleep(0.5)

    def slither_top(self):
        js = "var str=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        sleep(0.5)

    def slither_direc(self, loc_xpath):
        pass




