from OPS.login import Login_first
from selenium import webdriver
from time import *
import datetime
from OPS.Log.log import PrintLog
import unittest

logger = PrintLog()


class Brand(unittest.TestCase):
    """品牌管理流程测试"""
    logger.debug("票证类型流程测试")

    def setUpClass(self) -> None:
        t = Login_first("jgzh01", "su123456", "801B", "ops")
        self.driver = t.login()
        logger.debug("实例化Login类login方法")

    def test_1_add(self):
        """
        点击票证类型模块
        """
        self.driver.find_element_by_xpath('//*[@id="root"]/section/aside/div/a[8]/span').click()
        sleep(0.5)
        # 新增
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/div[1]/div[1]/form/div['
                                          '1]/div/div/span/button') .click()
        self.driver.find_element_by_id("name").send_keys("Automated Testing")
        # 上传图片
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[3]/div['
                                          '2]/div/span/span/div[1]/span/button') .click()

