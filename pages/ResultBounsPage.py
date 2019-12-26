import sys
sys.path.append("./")
from common.common import *

"""
introduction：个税计算器：计算年终奖结果页
author：黄思梦
date-last-modified：2019-12-26
last-modified-by：黄思梦
"""


class BounsTax(BasePages):
    loc_tax = "//*[@id='tax_result']/div[2]/div[15]"

    def get_tax(self):
        tax_text = self._find_ele('xpath', self.loc_tax).get_attribute('textContent')
        return float(tax_text)