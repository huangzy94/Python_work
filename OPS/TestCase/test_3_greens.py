from OPS.login import Login_first
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from OPS.Log.log import PrintLog
from time import *
import datetime
import unittest
import os

logger = PrintLog()


class Greens(unittest.TestCase):
    """菜品库流程测试"""
    logger.debug("菜品库流程测试")

    @classmethod  # 使用装饰器使装饰器下的方法仅运行一次
    def setUpClass(self) -> None:
        # 调用Login类的登录方法
        t = Login_first("jgzh01", "su123456", "801B", "ops")
        self.driver = t.login()
        logger.debug("菜品库流程测试开始")

    def test_1_menu(self):
        """新增菜品流程"""
        logger.debug("新增菜品流程")

        # 点击食材库模块
        logger.debug("点击食材库模块")
        self.driver.find_element_by_xpath('//*[@id="root"]/section/aside/div/a[4]/span').click()
        self.driver.find_element_by_class_name('ant-select-selection__placeholder').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"荤菜")]').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div[1]/div/form/div[1]/div['
                                          '2]/div/span/div/div/span[1]/i').click()
        input_value = '//*[@id="root"]/section/main/div/div[2]/div/div[1]/div/form/div[2]/div/div/span/span/input'
        self.driver.find_element_by_xpath(input_value).send_keys("海带排骨汤")
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div[1]/div/form/div['
                                          '2]/div/div/span/span/span/i').click()
        self.driver.implicitly_wait(10)
        # 按名称排序
        logger.debug("排序")
        a1 = '//*[@id="root"]/section/main/div/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[' \
             '2]/span/div/span[2]/div/i[1] '
        self.driver.find_element_by_xpath(a1).click()
        sleep(0.5)
        a2 = '//*[@id="root"]/section/main/div/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[' \
             '2]/span/div/span[2]/div/i[2] '
        self.driver.find_element_by_xpath(a2).click()
        sleep(0.5)
        # 按类别排序
        b1 = '//*[@id="root"]/section/main/div/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[' \
             '3]/span/div/span[2]/div/i[1] '
        self.driver.find_element_by_xpath(b1).click()
        b2 = '//*[@id="root"]/section/main/div/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[' \
             '3]/span/div/span[2]/div/i[2] '
        self.driver.find_element_by_xpath(b2).click()
        sleep(0.5)
        # 按标签排序
        c1 = '//*[@id="root"]/section/main/div/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[' \
             '6]/span/div/span[2]/div/i[1] '
        self.driver.find_element_by_xpath(c1).click()
        sleep(0.5)
        c2 = '//*[@id="root"]/section/main/div/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[' \
             '6]/span/div/span[2]/div/i[2] '
        self.driver.find_element_by_xpath(c2).click()
        sleep(0.5)
        # 切换标签状态
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div[1]/div/form/div['
                                          '3]/div/div/span/div/label[2]/span[2]').click()
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div[1]/div/form/div['
                                          '3]/div/div/span/div/label[1]/span[2]').click()
        # 新增菜品
        logger.debug("新增菜品")
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[2]/div/form/div[1]/div/div/span/button').click()
        self.driver.find_element_by_id('foodName').click()
        self.driver.find_element_by_id('foodName').send_keys("自动化测试菜品")
        self.driver.find_element_by_xpath('//*[@id="type"]/div/div/div').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"素菜")]').click()
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[2]/div[2]/form/div/div[3]/div/div[2]/div/span/span').click()
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[2]/div[2]/form/div/div[3]/div/div[2]/div/span/input').send_keys(
            "Automated Testing")
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[3]/div[2]/div/div/div/div/div/div[3]/button').click()
        sleep(1)
        # 食材选择
        self.driver.find_element_by_xpath('//*[@id="keywords"]/div/div/ul/li/div/input').send_keys("大米")
        sleep(0.5)
        # 模拟键盘回车添加sku
        self.driver.find_element_by_xpath('//*[@id="keywords"]/div/div/ul/li/div/input').send_keys(Keys.ENTER)
        sleep(0.5)
        # 清空已输入内容(为菜品添加两个食材)
        self.driver.find_element_by_xpath('//*[@id="keywords"]/div/div/ul/li/div/input').clear()
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="keywords"]/div/div/ul/li/div/input').send_keys("食用油")
        sleep(0.5)
        # 模拟键盘回车添加sku
        self.driver.find_element_by_xpath('//*[@id="keywords"]/div/div/ul/li/div/input').send_keys(Keys.ENTER)
        self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]').click()
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[3]/div[2]/div/div/div/div/div/div['
                                          '1]/table/tbody/tr[1]/td[3]/input').send_keys("360")
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[3]/div[2]/div/div/div/div/div/div['
                                          '1]/table/tbody/tr[2]/td[3]/input').send_keys("780")
        # 更换“食用油”的配菜用量单位
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[3]/div[2]/div/div/div/div/div/div['
                                          '1]/table/tbody/tr[2]/td[4]/div/div/div/div/div').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"瓶")]').click()
        self.driver.implicitly_wait(10)
        # 定位上传图片按钮
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[4]/div/div/div/span/div[1]/span/div/i').click()
        # 调用AutoIt脚本上传菜品图片
        logger.debug("调用AutoIt脚本上传菜品图片")
        os.system(r'D:\Python_work\AutoIt_Script\菜品图片.exe')
        sleep(2)
        # 烧制方法
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[5]/div[2]/div/div/div[2]/div/div/div').send_keys("Automated Testing")
        # 保存
        logger.debug("保存菜品")
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[6]/div[2]/button[2]').click()
        sleep(1)
        message = self.driver.find_element_by_xpath('/html/body/div[2]/div/span/div/div/div/span').get_attribute(
            "textContent")
        print(message)
        logger.debug(message)
        if message == "图片未上传":
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[6]/div[2]/button[2]').click()
        elif message == "未知错误":
            print("新增菜品：", message)
            logger.error(message)
            self.driver.close()
            logger.debug("流程意外终止")

    def test_2_list(self):
        """操作栏按钮功能回归"""
        print("操作栏按钮功能回归")
        logger.debug("操作栏按钮功能回归")

        # 查看已添加的菜品
        logger.debug("查看详情")
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div[1]/div/form/div['
                                          '2]/div/div/span/span/input').clear()
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div[1]/div/form/div['
                                          '2]/div/div/span/span/input').send_keys("自动化")
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div[1]/div/form/div['
                                          '2]/div/div/span/span/span/i').click()  # 搜索
        sleep(0.5)
        # 查看菜品详情
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div['
                                          '2]/div/div/div/div/div/table/tbody/tr/td[7]/a[1]').click()
        sleep(0.5)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[1]/div/div/div[2]/div/div[1]/div/button').click()
        # 编辑菜品
        logger.debug("编辑菜品")
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div['
                                          '2]/div/div/div/div/div/table/tbody/tr/td[7]/a[2]').click()
        sleep(0.5)
        # 删除食用油
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[3]/div[2]/div/div/div/div/div/div[1]/table/tbody/tr[2]/td[5]/a').click()
        # 保存
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[6]/div[2]/button[2]').click()
        sleep(0.5)
        # 删除菜品
        logger.debug("删除菜品")
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div['
                                          '2]/div/div/div/div/div/table/tbody/tr/td[7]/a[3]').click()
        self.driver.implicitly_wait(10)

    def test_3_delete(self):
        start = datetime.datetime.now()
        logger.debug("遍历字典找到想要的元素定位")
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        b = '/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        c = '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        d = '/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        e = '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        f = '/html/body/div[8]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        lists = [a, b, c, d, e, f]
        for element in lists:
            try:
                self.driver.find_element_by_xpath(element).click()        # 删除 二次确认
            except Exception as error:
                print(error)
                logger.error(error)
            else:
                print("菜品删除成功")
                logger.debug("菜品删除成功")
                end = datetime.datetime.now()
                print("test_3_delete 遍历耗时:", str(end-start))
                logger.debug("test_3_delete 遍历耗时:" + str(end-start))
                logger.warning("test_3_delete 遍历耗时:" + str(end-start))
                return element

        sleep(0.5)
        self.driver.refresh()
        self.driver.find_element_by_xpath('//*[@id="root"]/section/aside/div/a[4]/span').click()
        # 全选
        logger.debug("全选")
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/div['
                                          '2]/div/div/div/div/div/table/thead/tr/th[1]/span/div/span['
                                          '1]/div/label/span/input').click()
        # 定义/取消新品
        logger.debug("定义/取消新品")
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[2]/div/form/div[3]/div/div/span/button').click()
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[2]/div/form/div[4]/div/div/span/button').click()


def tearDownClass(self) -> None:
    self.driver = webdriver.Chrome()
    self.driver.close()
    print("菜品库流程测试结束")
    logger.debug("菜品库流程测试结束")


