from OPS.login import Login_first
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from OPS.Log.log import PrintLog
from time import *
import datetime
import unittest
import os

logger = PrintLog()  # 实例化日志类


class Food(unittest.TestCase):
    """食材库流程测试"""

    @classmethod  # 使用装饰器使装饰器下的方法仅运行一次
    def setUpClass(self) -> None:
        # 调用Login类的登录方法
        logger.debug("调用Login类的登录方法")
        t = Login_first("jgzh01", "su123456", "801B", "ops")
        try:
            self.driver = t.login()
        except Exception as error:
            logger.error(error)
        else:
            logger.debug("实例化Login类login方法")

    def test_1_food(self):
        """食材库"""
        # 定位“食材库”模块
        food = self.driver.find_element_by_xpath('//*[@id="root"]/section/aside/div/a[2]/span')
        try:
            food.click()
        except Exception as error:
            print("定位“食材库”模块fail:", error)
            logger.error(error)
        else:
            logger.debug('已定位到食材库模块')
        self.driver.implicitly_wait(10)  # 隐式等待-等待全局元素加载完成
        print("first:begin食材库测试流程")
        logger.debug("first:begin食材库测试流程")

        # 定位下拉框
        sleep(1)
        select = '//*[@id="root"]/section/main/div[2]/div/div[1]/div[1]/form/div[1]/div[2]/div/span/div/div/span/input'
        self.driver.find_element_by_xpath(select).click()
        sleep(0.5)

        # 使用text()方法定位到第一个下拉框的value
        self.driver.find_element_by_xpath('//li[contains(text(),"肉类")]').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"后腿肉")]').click()
        sleep(1)

        # 定位i标签清空图标data-icon="close-circle"
        em = '//*[@id="root"]/section/main/div[2]/div/div[1]/div[1]/form/div[1]/div[2]/div/span/div/div/span/i[1]'
        self.driver.find_element_by_xpath(em).click()
        sleep(0.5)

        # 定位搜索框并执行搜索
        food_key = '//*[@id="root"]/section/main/div[2]/div/div[1]/div[1]/form/div[2]/div/div/span/span/input'
        self.driver.find_element_by_xpath(food_key).send_keys("猪肉")
        food_search = '//*[@id="root"]/section/main/div[2]/div/div[1]/div[1]/form/div[2]/div/div/span/span/span/i'
        self.driver.find_element_by_xpath(food_search).click()
        sleep(0.5)
        # 清空输入框内容
        self.driver.find_element_by_xpath(food_key).clear()
        self.driver.find_element_by_xpath(food_search).click()
        sleep(0.5)

        # 按食材名称排序
        a1 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[2]/span/div/span[' \
             '2]/div/i[1] '
        self.driver.find_element_by_xpath(a1).click()
        a2 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[2]/span/div/span[' \
             '2]/div/i[2] '
        self.driver.find_element_by_xpath(a2).click()

        # 按上市季节排序
        b1 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[4]/span/div/span[' \
             '2]/div/i[1] '
        self.driver.find_element_by_xpath(b1).click()
        b2 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[4]/span/div/span[' \
             '2]/div/i[2] '
        self.driver.find_element_by_xpath(b2).click()

        # 按分类排序
        c1 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[5]/span/div/span[' \
             '2]/div/i[1] '
        self.driver.find_element_by_xpath(c1).click()
        c2 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[5]/span/div/span[' \
             '2]/div/i[2] '
        self.driver.find_element_by_xpath(c2).click()

        # 新增食材--基本属性
        logger.debug("新增食材")
        user_name = "自动化测试"
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div[2]/div/div[1]/div[2]/button[2]').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id('goodsName').send_keys(user_name)
        self.driver.find_element_by_xpath('//*[@id="unit"]/div/div/div').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"斤")]').click()
        category = '//*[@id="root"]/section/main/div/div[2]/div[2]/form/div[1]/div[3]/div/div/div/div[' \
                   '2]/div/span/span/span '
        self.driver.find_element_by_xpath(category).click()
        sleep(0.5)
        self.driver.find_element_by_xpath('//li[contains(text(),"乳品冷饮")]').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"低温奶")]').click()
        self.driver.find_element_by_xpath('//*[@id="season"]/div/div').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"全年")]').click()
        self.driver.find_element_by_xpath('//*[@id="inspection"]/div/div').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"计量验收")]').click()
        # 食材别名
        alias1 = '//*[@id="root"]/section/main/div/div[2]/div[2]/form/div[4]/div/div/div[2]/div/span'
        self.driver.find_element_by_xpath(alias1).click()
        alias2 = '//*[@id="root"]/section/main/div/div[2]/div[2]/form/div[4]/div/div/div[2]/div/span/input'
        self.driver.find_element_by_xpath(alias2).send_keys("ui自动化")
        # 票证类型
        self.driver.find_element_by_xpath('//*[@id="goodTicketTypes"]/div/div').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//li[contains(text(),"其他证明")]').click()
        self.driver.implicitly_wait(10)
        # 营养成分元素当前页面不可见，需要滚动滚动条使其可见
        js = "var q=document.documentElement.scrollTop=400"
        self.driver.execute_script(js)
        sleep(1)
        # 营养成分
        self.driver.find_element_by_id("rl").send_keys(100)
        self.driver.find_element_by_id("dbz").send_keys(100)
        sleep(0.5)
        # 滚到底部
        js = "var q=document.documentElement.scrollTop=1800"
        self.driver.execute_script(js)
        logger.debug("操作滚动条滚动到底部元素位置")
        sleep(1)
        self.driver.find_element_by_id("gai").send_keys(100)
        upload1 = '//*[@id="root"]/section/main/div/div[6]/div[2]/div[1]/span/div[1]/span/button'
        self.driver.find_element_by_xpath(upload1).click()
        sleep(1)
        # 调用AutoIt脚本实现文件上传
        os.system(r'D:\Python_work\AutoIt_Script\ops食材库优质样例图片.exe')
        sleep(3)
        logger.debug("调用AutoIt脚本实现文件上传")
        # 滚到底部
        js = "var q=document.documentElement.scrollTop=2000"
        self.driver.execute_script(js)
        sleep(2)
        upload2 = '//*[@id="root"]/section/main/div/div[6]/div[2]/div[2]/span/div[1]/span/button'
        self.driver.find_element_by_xpath(upload2).click()
        sleep(1)
        os.system(r'D:\Python_work\AutoIt_Script\ops食材库劣质样例图片.exe')
        sleep(5)
        # 保存并维护规格
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[7]/div[2]/button[3]').click()
        message = self.driver.find_element_by_xpath('/html/body/div[2]/div/span/div/div/div').get_attribute(
            'textContent')
        print(message)
        if message == "数据校验失败:商品名称已存在.":
            user_name1 = user_name + "1"
            # 滚动到顶部使元素可见
            js = "var q=document.documentElement.scrollTop=0"
            self.driver.execute_script(js)
            sleep(2)
            self.driver.find_element_by_id('goodsName').clear()
            self.driver.find_element_by_id('goodsName').send_keys(user_name1)
            self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[7]/div[2]/button[3]').click()  # 保存
            logger.warning("数据校验失败:食材名称已存在.")
            logger.debug("数据校验失败:食材名称已存在.")
        elif message == "未知错误":
            print("新增SKU:", message)
            logger.error(message)
            logger.debug("流程意外终止")
            self.driver.close()

        # 规格信息
        sleep(1)
        add1 = '//*[@id="root"]/section/main/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/button'
        try:
            self.driver.find_element_by_xpath(add1).click()
        except Exception as error:
            print("定位规格添加按钮fail", error)
            logger.error(error)
        else:
            logger.debug("规格添加按钮定位成功")
        img_button = '//*[@id="root"]/section/main/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[' \
                     '1]/table/tbody/tr/td[' \
                     '1]/span[2]/div[1]/span/button '
        self.driver.find_element_by_xpath(img_button).click()
        # 调用AutoIt脚本实现文件上传
        os.system(r'D:\Python_work\AutoIt_Script\规格图片.exe')
        logger.debug("调用AutoIt脚本上传规格图片")
        sleep(2)
        add2 = '//*[@id="root"]/section/main/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/table/tbody/tr/td[' \
               '2]/a[2] '
        self.driver.find_element_by_xpath(add2).click()
        # 返回
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[1]/div/div/div[2]/div/div[1]/div/button').click()
        logger.debug("操作栏功能按钮回归")
        # 查看已添加的食材
        self.driver.find_element_by_xpath(food_key).clear()
        self.driver.find_element_by_xpath(food_key).send_keys("自动化测试")
        self.driver.find_element_by_xpath(food_search).click()
        sleep(0.5)

        # 编辑
        editor = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr/td[6]/a[3]'
        self.driver.find_element_by_xpath(editor).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[7]/div[2]/button[2]').click()

        # 关键字搜索
        self.driver.find_element_by_xpath(food_key).clear()
        self.driver.find_element_by_xpath(food_key).send_keys("自动化测试")
        self.driver.find_element_by_xpath(food_search).click()
        sleep(0.5)
        # 规格详情
        sp_details = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a[1]'
        self.driver.find_element_by_xpath(sp_details).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[1]/div/div/div[2]/div/div[1]/div/button').click()

        # 关键字搜索
        self.driver.find_element_by_xpath(food_key).clear()
        self.driver.find_element_by_xpath(food_key).send_keys("自动化测试")
        self.driver.find_element_by_xpath(food_search).click()
        sleep(0.5)
        # 食材详情
        food_details = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a[2]'
        self.driver.find_element_by_xpath(food_details).click()
        sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[1]/div/div/div[2]/div/div[1]/div/button').click()

        # 关键字搜索
        self.driver.find_element_by_xpath(food_key).clear()
        self.driver.find_element_by_xpath(food_key).send_keys("自动化测试")
        self.driver.find_element_by_xpath(food_search).click()
        sleep(0.5)
        # 删除食材
        food_delete = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a[4]'
        self.driver.find_element_by_xpath(food_delete).click()
        sleep(0.5)
        logger.debug("操作栏功能按钮测试完成")

    def test_2_delete(self):
        start = datetime.datetime.now()
        logger.debug("遍历字典找到想要的元素定位")
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        b = '/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        c = '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        d = '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        e = '/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        f = '/html/body/div[8]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'
        lists = [a, b, c, d, e, f]
        for element in lists:
            try:
                self.driver.find_element_by_xpath(element).click()  # 删除 二次确认
            except Exception as error:
                print(error)
            else:
                print("食材删除成功")
                logger.debug("食材删除成功")
                end = datetime.datetime.now()
                print("test_2_delete 遍历耗时：", str(end - start))
                logger.debug("test_2_delete 遍历耗时："+str(end - start))
                logger.warning("test_2_delete 遍历耗时："+str(end - start))
                return element
        sleep(0.5)
        print("end:食材库测试流程结束")
        logger.debug("end:食材库测试流程结束")

    def test_3_To_audit(self):
        """食材库--待审核食材库"""
        logger.debug("食材库--待审核食材库")
        sleep(1)
        # 待审核食材库
        to_audit = '//*[@id="root"]/section/main/div[1]/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]'
        self.driver.find_element_by_xpath(to_audit).click()
        sleep(0.5)
        # 通过申请
        allow = '//*[@id="root"]/section/main/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[7]/a[1]'
        self.driver.find_element_by_xpath(allow).click()
        self.driver.find_element_by_xpath('//*[@id="keywords"]/div/div/ul/li/div/input').send_keys("饼干")
        sleep(0.5)
        logger.debug("通过申请")
        # 模拟键盘回车添加sku
        self.driver.find_element_by_xpath('//*[@id="keywords"]/div/div/ul/li/div/input').send_keys(Keys.ENTER)
        sleep(0.5)

    def test_4_save(self):
        start = datetime.datetime.now()
        logger.debug("遍历字典找到想要的元素定位")
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        b = '/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        c = '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        d = '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        e = '/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        f = '/html/body/div[8]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        g = '/html/body/div[9]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        h = '/html/body/div[10]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        lists = [a, b, c, d, e, f, g, h]
        for element in lists:
            try:
                self.driver.find_element_by_xpath(element).click()  # 食材选择-保存按钮
            except Exception as error:
                print(error)
                logger.error(error)
            else:
                print("食材审核通过")
                logger.debug("食材审核通过")
                end = datetime.datetime.now()
                print("test_4_save 遍历耗时：", str(end - start))
                logger.debug("test_2_delete 遍历耗时："+str(end - start))
                logger.warning("test_2_delete 遍历耗时："+str(end - start))
                return element
        sleep(0.5)

    def test_5_send(self):
        start = datetime.datetime.now()
        # 拒绝申请
        sleep(1)
        refuse = '//*[@id="root"]/section/main/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[7]/a[2]'
        self.driver.find_element_by_xpath(refuse).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("replyContent").send_keys("自动化test-未上市")
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[7]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        b = '/html/body/div[8]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        c = '/html/body/div[5]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        d = '/html/body/div[6]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        e = '/html/body/div[4]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        f = '/html/body/div[3]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        lists = [a, b, c, d, e, f]
        for element in lists:
            try:
                self.driver.find_element_by_xpath(element).click()  # # 审核不通过 发送按钮
            except Exception as error:
                print(error)
                logger.error(error)
            else:
                print("食材审核已拒绝")
                end = datetime.datetime.now()
                print("test_5_send 遍历耗时：", str(end - start))
                logger.debug("test_2_delete 遍历耗时："+str(end - start))
                logger.warning("test_2_delete 遍历耗时："+str(end - start))
                return element

        print("食材库流程测试完成！")
        logger.debug("食材库流程测试完成！")
        print("----------------------------------------------------------------------")

    @classmethod
    def tearDownClass(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.close()
        print("关闭浏览器")
        logger.debug("关闭浏览器")
