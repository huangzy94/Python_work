from OPS.login import Login_first
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import *
import datetime
from OPS.Log.log import PrintLog
import unittest

logger = PrintLog()


class Brand(unittest.TestCase):
    """用户管理流程测试"""
    logger.debug("用户管理流程测试")

    @classmethod  # 使用装饰器使装饰器下的方法仅运行一次
    def setUpClass(self) -> None:
        t = Login_first("jgzh01", "su123456", "801B", "ops")
        self.driver = t.login()
        logger.debug("实例化Login类login方法")

    def test_1_superior(self):
        """
        餐饮管理单位模块
        """
        logger.debug("添加管理单位流程开始----------------------------------------------------------------------")
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/aside/div/a[10]/span').click()
        # 新增
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[2]/div/form[2]/div[1]/div/div/span/button').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('Automated Testing')
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('su123456')
        self.driver.find_element(By.XPATH, '//*[@id="superiorName"]').send_keys('自动化测试教育局')
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('120056@qq.com')
        self.driver.find_element(By.XPATH, '//*[@id="mobile"]').send_keys('18600174391')
        self.driver.find_element(By.XPATH, '//*[@id="zoneId"]').send_keys("\n")
        self.driver.find_element(By.XPATH, '//li[contains(text(),"北京市")]').click()
        self.driver.find_element(By.XPATH, '//li[contains(text(),"东城区")]').click()
        self.driver.find_element(By.XPATH, '//*[@id="authModules"]/label[1]/span[1]/input').click()
        sleep(1)

        # 保存信息
    def test_2_add1(self):
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
                self.driver.find_element_by_xpath(add).click()  # 保存账户信息
            except Exception as error:
                logger.error(error)
            else:
                ad = add
                print("管理单位新增成功")
                end = datetime.datetime.now()
                print("test_2_add1 遍历耗时：", str(end - start))
                logger.debug("test_2_add1 遍历耗时：" + str(end - start))
                logger.warning("test_2_add1 遍历耗时：" + str(end - start))
                return ad
        # 启用账户
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div['
                                           '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/a[2]').click()

    def test_3_catering(self):
        """
        餐饮单位模块
        """
        logger.debug("添加餐饮单位流程开始----------------------------------------------------------------------")
        # 切换到餐饮单位tab
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[1]/div/div[2]/div['
                                           '1]/div/div/div/div/div[1]/div[2]').click()
        sleep(1)
        # 新增
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[2]/div/form[2]/div[1]/div/div/span/button').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('Automated Testing1')
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('su123456')
        self.driver.find_element(By.XPATH, '//*[@id="cateringName"]').send_keys('自动化测试中学')
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('1200156@qq.com')
        self.driver.find_element(By.XPATH, '//*[@id="zoneId"]').send_keys("\n")
        self.driver.find_element(By.XPATH, '//li[contains(text(),"北京市")]').click()
        self.driver.find_element(By.XPATH, '//li[contains(text(),"东城区")]').click()
        self.driver.find_element(By.XPATH, '//*[@id="superiorId"]/div/div').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//li[contains(text(),"自动化测试教育局")]').click()
        self.driver.find_element(By.XPATH, '//*[@id="administrator"]').send_keys('李云龙')
        self.driver.find_element(By.XPATH, '//*[@id="mobile"]').send_keys('18600174392')
        self.driver.find_element(By.XPATH, '//*[@id="oriented"]/div/div').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//li[contains(text(),"初中")]').click()

        # 保存信息
    def test_4_add2(self):
        save1 = ad
        sleep(0.5)
        self.driver.find_element(By.XPATH, save1).click()
        sleep(1)

        # 关键字搜索
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[2]/div/form[1]/div['
                                           '3]/div/div/span/span/input').send_keys('自动化')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[2]/div/form[1]/div['
                                           '3]/div/div/span/span/input').send_keys(Keys.ENTER)
        # 操作栏-更多
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div['
                                           '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/a[4]').click()

        # 启用账户
        logger.debug("遍历字典找到想要的元素定位")
        print("遍历字典找到想要的元素定位")
        start = datetime.datetime.now()
        a = '/html/body/div[2]/div/div/ul/li[5]/a'
        b = '/html/body/div[3]/div/div/ul/li[5]/a'
        c = '/html/body/div[4]/div/div/ul/li[5]/a'
        d = '/html/body/div[5]/div/div/ul/li[5]/a'
        e = '/html/body/div[6]/div/div/ul/li[5]/a'
        f = '/html/body/div[7]/div/div/ul/li[5]/a'
        g = '/html/body/div[8]/div/div/ul/li[5]/a'
        h = '/html/body/div[9]/div/div/ul/li[5]/a'
        lists = [a, b, c, d, e, f, g, h]
        for using in lists:
            try:
                self.driver.find_element(By.XPATH, using).click()
            except Exception as error:
                logger.debug(error)
            else:
                logger.debug('当前定位的元素为：' + using)
                print("账户启用成功")
                end = datetime.datetime.now()
                print("test_4_add2 遍历耗时：", str(end - start))
                logger.debug("test_4_add2 遍历耗时：" + str(end - start))
                logger.warning("test_4_add2 遍历耗时：" + str(end - start))
                return using

    def test_5_delete(self):
        # 操作栏-更多
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div['
                                           '2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[8]/a[4]').click()

        # 删除账户
        global delete1
        logger.debug("遍历字典找到想要的元素定位")
        print("遍历字典找到想要的元素定位")
        start = datetime.datetime.now()
        a = '/html/body/div[2]/div/div/ul/li[2]/a'
        b = '/html/body/div[3]/div/div/ul/li[2]/a'
        c = '/html/body/div[4]/div/div/ul/li[2]/a'
        d = '/html/body/div[5]/div/div/ul/li[2]/a'
        e = '/html/body/div[6]/div/div/ul/li[2]/a'
        f = '/html/body/div[7]/div/div/ul/li[2]/a'
        g = '/html/body/div[8]/div/div/ul/li[2]/a'
        h = '/html/body/div[9]/div/div/ul/li[2]/a'
        lists = [a, b, c, d, e, f, g, h]
        for delete in lists:
            try:
                self.driver.find_element(By.XPATH, delete).click()
            except Exception as error:
                logger.debug(error)
            else:
                logger.debug('当前定位的元素为：' + delete)
                delete1 = delete
                print("账户删除成功")
                end = datetime.datetime.now()
                print("test_5_delete 遍历耗时：", str(end - start))
                logger.debug("test_5_delete 遍历耗时：" + str(end - start))
                logger.warning("test_5_delete 遍历耗时：" + str(end - start))
                return delete1

    def test_6_ensure(self):
        # 确认操作
        sleep(1)
        start = datetime.datetime.now()
        logger.debug("遍历字典找到想要的元素定位")
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        b = '/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        c = '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        d = '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        e = '/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        f = '/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        g = '/html/body/div[8]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        h = '/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        lists = [a, b, c, d, e, f, g, h]
        for ensure1 in lists:
            try:
                # 此处拼接元素
                self.driver.find_element_by_xpath(ensure1).click()  # 确定删除
            except Exception as error:
                logger.error(error)
            else:
                print("删除成功，当前定位元素为：" + ensure1)
                end = datetime.datetime.now()
                print("test_6_ensure 遍历耗时：", str(end - start))
                logger.debug("test_6_ensure 遍历耗时：" + str(end - start))
                logger.warning("test_6_ensure 遍历耗时：" + str(end - start))
        logger.debug('餐饮单位流程结束----------------------------------------------------------------------')

        # 切换到餐饮管理单位tab，删除新增的管理单位
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[1]/div/div[2]/div['
                                           '1]/div/div/div/div/div[1]/div[1]').click()

        # 关键字搜索
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[2]/div/form[1]/div['
                                           '3]/div/div/span/span/input').send_keys('自动化')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[2]/div/form[1]/div['
                                           '3]/div/div/span/span/input').send_keys(Keys.ENTER)

        # 删除管理单位账户
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div['
                                           '2]/div/div/div/div/div/div/div/table/tbody/tr/td[8]/a[3]').click()

        # 调用test_6_ensure定位的元素，二次确认
        sleep(0.5)
        for ensure2 in lists:
            try:
                # 此处拼接元素
                self.driver.find_element_by_xpath(ensure2).click()  # 确定删除
            except Exception as error:
                logger.error(error)
            else:
                print("删除成功，当前定位元素为：" + ensure2)
                end = datetime.datetime.now()
                print("test_6_ensure2 遍历耗时：", str(end - start))
                logger.debug("test_6_ensure2 遍历耗时：" + str(end - start))
                logger.warning("test_6_ensure2 遍历耗时：" + str(end - start))
        logger.debug('餐饮管理单位流程结束----------------------------------------------------------------------')

        logger.debug('添加供货商流程开始----------------------------------------------------------------------')
        # 切换到供货商tab
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[1]/div/div[2]/div['
                                           '1]/div/div/div/div/div[1]/div[3]').click()
        # 新增
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[2]/div/form[2]/div[1]/div/div/span/button').click()
        sleep(0.5)
        self.driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('Automated Testing2')
        self.driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('su123456')
        self.driver.find_element(By.XPATH, '//*[@id="supplierName"]').send_keys('自动化测试供货商')
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('0120056@qq.com')
        self.driver.find_element(By.XPATH, '//*[@id="zoneId"]').send_keys("\n")
        self.driver.find_element(By.XPATH, '//li[contains(text(),"北京市")]').click()
        self.driver.find_element(By.XPATH, '//li[contains(text(),"东城区")]').click()
        self.driver.find_element(By.XPATH, '//*[@id="mobile"]').send_keys('18600174393')
        self.driver.find_element(By.XPATH, '//*[@id="corporation"]').send_keys('李云龙')
        sleep(0.5)

        # 调用test_2_add1定位的元素,保存信息
        save2 = ad
        self.driver.find_element(By.XPATH, save2).click()

        # 关键字搜索
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[2]/div/form[1]/div['
                                           '3]/div/div/span/span/input').send_keys('自动化')
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div[2]/div/form[1]/div['
                                           '3]/div/div/span/span/input').send_keys(Keys.ENTER)

        # 删除供货商账户
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="root"]/section/main/div['
                                           '2]/div/div/div/div/div/div/div/table/tbody/tr/td[8]/a[3]').click()

        # 调用Global定位的元素，二次确认
        sleep(0.5)
        for ensure3 in lists:
            try:
                # 此处拼接元素
                self.driver.find_element_by_xpath(ensure3).click()  # 确定删除
            except Exception as error:
                logger.error(error)
            else:
                print("删除成功，当前定位元素为：" + ensure3)
                end = datetime.datetime.now()
                print("test_6_ensure3 遍历耗时：", str(end - start))
                logger.debug("test_6_ensure3 遍历耗时：" + str(end - start))
                logger.warning("test_6_ensure3 遍历耗时：" + str(end - start))
        logger.debug("供货商流程结束----------------------------------------------------------------------")


