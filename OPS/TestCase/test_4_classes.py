from selenium import webdriver
from OPS.login import Login_first
from time import *
import unittest
import datetime


class Classes(unittest.TestCase):
    """
    类别管理
    """

    @classmethod  # 使用装饰器使装饰器下的方法仅运行一次
    def setUpClass(self) -> None:
        t = Login_first("jgzh01", "su123456", "801B", "ops")
        self.driver = t.login()
        print("类别管理流程测试开始")

    def test_1_Food_category(self):
        """食材类别流程"""
        self.driver.find_element_by_xpath('//*[@id="root"]/section/aside/div/a[6]/span').click()    # 类别管理模块
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/form/div[1]/div/div/span/button').click()
        sleep(0.5)
        self.driver.find_element_by_id('catalogName').send_keys("Automated Testing")

    def test_2_confirm(self):
        global x
        start = datetime.datetime.now()
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[3]/div/div/div/div[2]/div/p[2]/button[2]'
        b = '/html/body/div[4]/div/div/div/div[2]/div/p[2]/button[2]'
        c = '/html/body/div[5]/div/div/div/div[2]/div/p[2]/button[2]'
        d = '/html/body/div[6]/div/div/div/div[2]/div/p[2]/button[2]'
        e = '/html/body/div[7]/div/div/div/div[2]/div/p[2]/button[2]'
        f = '/html/body/div[8]/div/div/div/div[2]/div/p[2]/button[2]'
        g = '/html/body/div[2]/div/div/div/div[2]/div/p[2]/button[2]'
        lists = [a, b, c, d, e, f, g]
        for element in lists:
            try:
                self.driver.find_element_by_xpath(element).click()
            except Exception as error:
                print(error)
            else:
                print("类别添加成功:", element)
                x = element
                end = datetime.datetime.now()
                print("test_2_confirm 遍历耗时:", str(end - start))
                return element
        message = self.driver.find_element_by_xpath('/html/body/div[2]/div/span/div/div/div/span').get_attribute(
            'textContent')
        print(message)
        sleep(0.5)
        if message == "数据校验失败:类别名称已存在.":
            name = "Automated Testing Testing"
            sleep(1)
            self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/form/div['
                                              '1]/div/div/span/button').click()
            sleep(0.5)
            self.driver.find_element_by_id('catalogName').send_keys(name)
            sleep(0.5)
            # 确定
            self.driver.find_element_by_xpath(x).click()
        elif message == "未知错误":
            print("新增SKU：", message)
            self.driver.close()

    def test_3_edit(self):
        print("操作栏功能按钮回归")
        sleep(0.5)
        # 调用函数2的返回值
        e = x
        # 编辑
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div['
                                          '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/a[1]') .click()
        sleep(0.5)
        self.driver.find_element_by_xpath(e).click()
        # 添加下级分类
        sleep(1)
        add = '//*[@id="root"]/section/main/div/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/a[3]'
        self.driver.find_element_by_xpath(add).click()
        self.driver.find_element_by_id('catalogName').send_keys("Testing")
        sleep(0.5)
        self.driver.find_element_by_xpath(e).click()
        print("添加下级分类成功")
        sleep(0.5)
        # 展开下级分类
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div['
                                          '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/div') .click()
        sleep(0.5)
        # 子类排序
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div['
                                          '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/span[2]/a') .click()
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div['
                                          '2]/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div/div[2]/input') .send_keys("1")
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div['
                                          '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[1]/span[2]/a[1]') .click()

    def test_4_delete(self):
        global p
        start = datetime.datetime.now()
        # 删除下级分类
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div['
                                          '2]/div/div/div/div/div/div/div/table/tbody/tr[2]/td[3]/a[2]') .click()
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        b = '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        c = '/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        d = '/html/body/div[8]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        e = '/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        f = '/html/body/div[7/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        g = '/html/body/div[10]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        lists = [a, b, c, d, e, f, g]
        for button in lists:
            try:
                self.driver.find_element_by_xpath(button).click()
            except Exception as error:
                print("定位失败", error)
            else:
                print('下级分类删除成功', button)
                p = button
                end = datetime.datetime.now()
                print("test_4_delete 遍历耗时：", str(end - start))
                return button
        sleep(1)
        # 删除主类
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div['
                                          '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/a[2]') .click()
        self.driver.find_element_by_xpath(p).click()

    def test_5_ingredients_category(self):
        sleep(1)
        # 辅料类别
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[1]/div/div[2]/div['
                                          '1]/div/div/div/div/div[1]/div[2]') .click()
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/form/div[1]/div/div/span/button').click()
        self.driver.find_element_by_id('catalogName').send_keys("Testing")
        sleep(0.5)
        button = x
        # 保存主类别
        self.driver.find_element_by_xpath(button).click()
        sleep(0.5)
        # 编辑
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div['
                                          '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/a[1]') .click()
        self.driver.find_element_by_xpath(button).click()
        sleep(1)
        # 排序
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/form/div['
                                          '2]/div/div/span/div/button') .click()
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div['
                                          '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/div/div['
                                          '2]/input').send_keys("1")
        # 保存
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[2]/div/form/div['
                                          '2]/div/div/span/div/button[1]') .click()
        sleep(0.5)
        # 删除类别
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div['
                                          '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/a[2]') .click()
        delete = p
        self.driver.find_element_by_xpath(delete).click()
        print("类别管理流程测试完成！")
        print("----------------------------------------------------------------------")

    @classmethod
    def tearDownClass(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.close()
        print("关闭浏览器")







