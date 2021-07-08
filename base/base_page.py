"""
@Time 2021/07/08
@Author Wendy Liang
@Content base_page.py
"""

class basePage:
    def __init__(self):
        self.driver = driver

    def locator_ele(self, loc):
        return self.driver.find_element(*loc)

    def click(self, loc):
        self.locator_ele(loc).click()
