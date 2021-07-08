"""
@Time 2021/07/08
@Author Wendy Liang
@Content base_init.py
"""
import unittest

import pytest

from selenium import webdriver

class BaseUtil(unittest.TestCase):
    def setUp(self) -> None:
        global driver
        self.driver = webdriver.Chrome()
        driver = self.driver
        self.driver.get('https://crypto.com/exchange/?type=spot')

    def tearDown(self) -> None:
        pass