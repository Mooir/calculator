import sys
sys.path.append("./")
from common.common import *


class BounsTax(BasePages):
    loc_tax = "//*[@id='tax_result']/div[2]/div[15]"

    def get_tax(self):
        tax_text = self._find_ele('xpath', self.loc_tax).get_attribute('textContent')
        return float(tax_text)