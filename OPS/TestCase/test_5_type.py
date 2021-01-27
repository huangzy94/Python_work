from OPS.login import Login_first
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from OPS.Log.log import PrintLog
from selenium import webdriver
from time import *
import datetime
import os
import unittest

logger = PrintLog()


class Brand(unittest.TestCase):
    """品牌管理流程测试"""
    logger.debug("票证类型流程测试")

    @classmethod  # 使用装饰器使装饰器下的方法仅运行一次
    def setUpClass(self) -> None:
        t = Login_first("jgzh01", "su123456", "801B", "ops")
        self.driver = t.login()
        logger.debug("实例化Login类login方法")

    def test_1_add(self):
        """
        点击票证类型模块
        """
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/aside/div/a[8]/span').click()
        sleep(0.5)
        # 新增
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div/div[1]/div[1]/form/div['
                                          '1]/div/div/span/button') .click()
        self.driver.find_element_by_id("name").send_keys("Automated Testing")
        # 上传图片
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[3]/div['
                                          '2]/div/span/span/div[1]/span/button') .click()
        sleep(2)
        # 调用AutoIt脚本实现文件上传
        os.system(r'D:\Python_work\AutoIt_Script\动物检测证明.exe')
        sleep(2)

        # 确认新增
    def test_2_add(self):
        global ad
        start = datetime.datetime.now()
        logger.debug("遍历字典找到想要的元素定位")
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        b = '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        c = '/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        d = '/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        e = '/html/body/div[6]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        f = '/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        g = '/html/body/div[8]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        h = '/html/body/div[9]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        lists = [a, b, c, d, e, f, g, h]
        for add in lists:
            try:
                self.driver.find_element_by_xpath(add).click()  # 确认添加票证
            except Exception as error:
                logger.error(error)
            else:
                ad = add
                print("票证添加成功")
                end = datetime.datetime.now()
                print("test_2_add 遍历耗时：", str(end-start))
                logger.debug("test_2_add 遍历耗时：" + str(end-start))
                logger.warning("test_2_add 遍历耗时：" + str(end-start))
                return ad

    def test_3_relevance(self):
        sleep(2)
        # 关联商品
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div/div/div['
                                           '2]/div/div/div/div/div/table/tbody/tr[1]/td[4]/a[1]').click()
        sleep(1)
        # 搜索商品
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div['
                                           '1]/div/div/form/div[2]/div/div/span/span/input').send_keys('牛肉')
        # 模拟键盘Enter键操作回车
        self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div['
                                           '1]/div/div/form/div[2]/div/div/span/span/input').send_keys(Keys.ENTER)
        sleep(1)
        start = datetime.datetime.now()
        logger.debug("遍历字典找到想要的元素定位")
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div[1]'
        b = '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]'
        c = '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]'
        d = '/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div[1]'
        e = '/html/body/div[6]/div/div[2]/div/div[2]/div[2]/div/div[1]'
        f = '/html/body/div[7]/div/div[2]/div/div[2]/div[2]/div/div[1]'
        g = '/html/body/div[8]/div/div[2]/div/div[2]/div[2]/div/div[1]'
        h = '/html/body/div[9]/div/div[2]/div/div[2]/div[2]/div/div[1]'
        lists = [a, b, c, d, e, f, g, h]
        # 拆分元素，后面用于拼接
        m = '/div/div/div/div/div/div/div/div/div[1]/table/thead/tr/th[3]/span/div/span[1]/a'
        for relevance in lists:
            try:
                # 此处拼接元素
                self.driver.find_element_by_xpath(relevance+m).click()  # 添加全部商品
            except Exception as error:
                logger.error(error)
            else:
                print("全部添加成功")
                end = datetime.datetime.now()
                print("test_3_relevance 遍历耗时：", str(end - start))
                logger.debug("test_3_relevance 遍历耗时：" + str(end - start))
                logger.warning("test_3_relevance 遍历耗时：" + str(end - start))
                return relevance

    def test_4_confirm(self):
        start = datetime.datetime.now()
        logger.debug("遍历字典找到想要的元素定位")
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        b = '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        c = '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        d = '/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        e = '/html/body/div[6]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        f = '/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        g = '/html/body/div[8]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        h = '/html/body/div[9]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        lists = [a, b, c, d, e, f, g, h]
        for confirm in lists:
            try:
                # 此处拼接元素
                self.driver.find_element_by_xpath(confirm).click()  # 确定结果
            except Exception as error:
                logger.error(error)
            else:
                print("商品关联成功")
                end = datetime.datetime.now()
                print("test_4_confirm 遍历耗时：", str(end - start))
                logger.debug("test_4_confirm 遍历耗时：" + str(end - start))
                logger.warning("test_4_confirm 遍历耗时：" + str(end - start))
                return confirm

    def test_5_edit(self):
        sleep(0.5)
        # 编辑
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div/div/div['
                                           '2]/div/div/div/div/div/table/tbody/tr[1]/td[4]/a[2]') .click()
        sleep(1)
        # 调用test_2_add函数的返回值 a
        delete = ad
        self.driver.find_element(By.XPATH, delete).click()
        sleep(1)
        # 删除
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div/div/div['
                                           '2]/div/div/div/div/div/table/tbody/tr[1]/td[4]/a[3]') .click()

    def test_6_delete(self):
        # 确认操作
        sleep(1)
        start = datetime.datetime.now()
        logger.debug("遍历字典找到想要的元素定位")
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[7]/div/div/div/div[2]/div/div/div[2]/button[2]'
        b = '/html/body/div[6]/div/div/div/div[2]/div/div/div[2]/button[2]'
        c = '/html/body/div[5]/div/div/div/div[2]/div/div/div[2]/button[2]'
        d = '/html/body/div[4]/div/div/div/div[2]/div/div/div[2]/button[2]'
        e = '/html/body/div[3]/div/div/div/div[2]/div/div/div[2]/button[2]'
        f = '/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/button[2]'
        g = '/html/body/div[8]/div/div/div/div[2]/div/div/div[2]/button[2]'
        h = '/html/body/div[9]/div/div/div/div[2]/div/div/div[2]/button[2]'
        lists = [a, b, c, d, e, f, g, h]
        for delete in lists:
            try:
                # 此处拼接元素
                self.driver.find_element_by_xpath(delete).click()  # 确定删除
            except Exception as error:
                logger.error(error)
            else:
                print("删除成功")
                end = datetime.datetime.now()
                print("test_6_delete 遍历耗时：", str(end - start))
                logger.debug("test_6_delete 遍历耗时：" + str(end - start))
                logger.warning("test_6_delete 遍历耗时：" + str(end - start))
                return delete

            print("票证类型流程测试完成！")
            logger.debug("票证类型流程测试完成！")
            print("----------------------------------------------------------------------")

    @classmethod
    def tearDownClass(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.close()
        logger.debug("关闭浏览器")



