from OPS.login import Login_first
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import *
import datetime
import unittest
import os


class Ingredients(unittest.TestCase):

    @classmethod  # 使用装饰器使装饰器下的方法仅运行一次
    def setUpClass(self) -> None:
        # 调用Login_first类中的登录方法
        t = Login_first("jgzh01", "su123456", "801B", "ops")
        self.driver = t.login()

    def test_1_library(self):
        """辅料库"""
        # 定位“辅料库”模块
        food = self.driver.find_element_by_xpath('//*[@id="root"]/section/aside/div/a[3]/span')
        try:
            food.click()
        except Exception as error:
            print("定位“辅料”模块fail:", error)
        self.driver.implicitly_wait(10)  # 隐式等待-等待全局元素加载完成
        print("second:begin辅料库测试流程...")
        s = self.driver.title
        print(s)

        # 定位下拉框
        sleep(1)
        select2 = '//*[@id="root"]/section/main/div[2]/div/div[1]/div[1]/form/div[1]/div[' \
                  '2]/div/span/div/div/div/div/div/div '
        self.driver.find_element_by_xpath(select2).click()
        sleep(0.5)

        # 使用text()方法定位下拉框的value
        self.driver.find_element_by_xpath('//li[contains(text(),"食用油")]').click()
        sleep(0.5)

        # 定位i标签清空图标data-icon="close-circle"
        em1 = '//*[@id="root"]/section/main/div[2]/div/div[1]/div[1]/form/div[1]/div[' \
              '2]/div/span/div/div/div/div/span[1]/i '
        self.driver.find_element_by_xpath(em1).click()
        sleep(0.5)

        # 定位搜索框并执行搜索
        food_key1 = '//*[@id="root"]/section/main/div[2]/div/div[1]/div[1]/form/div[2]/div/div/span/span/input'
        self.driver.find_element_by_xpath(food_key1).send_keys("食用小苏打")
        food_search1 = '//*[@id="root"]/section/main/div[2]/div/div[1]/div[1]/form/div[2]/div/div/span/span/span/i'
        self.driver.find_element_by_xpath(food_search1).click()
        sleep(0.5)
        # 清空输入框内容
        self.driver.find_element_by_xpath(food_key1).clear()
        self.driver.find_element_by_xpath(food_search1).click()
        sleep(0.5)

        # 按辅料名称排序
        a1 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[2]/span/div/span[' \
             '2]/div/i[1] '
        self.driver.find_element_by_xpath(a1).click()
        a2 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[2]/span/div/span[' \
             '2]/div/i[2] '
        self.driver.find_element_by_xpath(a2).click()

        # 按分类排序
        b1 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[4]/span/div/span[' \
             '2]/div/i[1] '
        self.driver.find_element_by_xpath(b1).click()
        b2 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[4]/span/div/span[' \
             '2]/div/i[2] '
        self.driver.find_element_by_xpath(b2).click()

        # 按储存方法排序
        c1 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[5]/span/div/span[' \
             '2]/div/i[1] '
        self.driver.find_element_by_xpath(c1).click()
        c2 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/thead/tr/th[5]/span/div/span[' \
             '2]/div/i[2] '
        self.driver.find_element_by_xpath(c2).click()
        sleep(0.5)

        # 新增辅料--基本属性
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div[2]/div/div[1]/div[2]/button[2]').click()
        self.driver.implicitly_wait(10)
        user_name = "自动化测试"
        self.driver.find_element_by_id('goodsName').send_keys(user_name)
        self.driver.find_element_by_xpath('//*[@id="catalogId"]/div/div/div').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"食用油")]').click()
        storage = '//*[@id="storage"]/div/div/div'
        self.driver.find_element_by_xpath(storage).click()
        self.driver.find_element_by_xpath('//li[contains(text(),"常温保存")]').click()
        self.driver.find_element_by_xpath('//*[@id="inspection"]/div/div/div').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"计量验收")]').click()
        self.driver.find_element_by_xpath('//*[@id="unit"]/div/div/div').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"斤")]').click()
        self.driver.find_element_by_xpath('//*[@id="goodTicketTypes"]/div/div/div').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"其他证明")]').click()
        # 营养成分
        self.driver.find_element_by_id("rl").send_keys(100)
        self.driver.find_element_by_id("dbz").send_keys(100)
        sleep(0.5)
        # 滚到底部
        js = "var q=document.documentElement.scrollTop=1800"
        self.driver.execute_script(js)
        sleep(1)
        self.driver.find_element_by_id("gai").send_keys(100)
        # 上传文件可使用send.keys方法，但要注意文件路径需要r进行转义
        upload3 = '//*[@id="root"]/section/main/div/div[6]/div[2]/div[1]/span/div[1]/span/button'
        self.driver.find_element_by_xpath(upload3).click()
        sleep(1)
        # 调用AutoIt脚本实现文件上传
        os.system(r'D:\Python_work\AutoIt_Script\ops食材库优质样例图片.exe')
        sleep(3)
        # 滚到底部
        js = "var q=document.documentElement.scrollTop=2000"
        self.driver.execute_script(js)
        sleep(2)
        upload4 = '//*[@id="root"]/section/main/div/div[6]/div[2]/div[2]/span/div[1]/span/button'
        self.driver.find_element_by_xpath(upload4).click()
        sleep(1)
        os.system(r'D:\Python_work\AutoIt_Script\ops食材库劣质样例图片.exe')
        sleep(5)
        # 保存并维护规格
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[7]/div[2]/button[3]').click()
        message = self.driver.find_element_by_xpath('/html/body/div[2]/div/span/div/div/div/span').get_attribute(
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
        elif message == "未知错误":
            print("新增SKU：", message)
            self.driver.close()

        # 规格信息
        sleep(1)
        add1 = '//*[@id="root"]/section/main/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/button'
        try:
            self.driver.find_element_by_xpath(add1).click()
        except Exception as error:
            print("定位规格添加按钮fail", error)
        img_button1 = '//*[@id="root"]/section/main/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[' \
                      '1]/table/tbody/tr/td[' \
                      '4]/span[2]/div[1]/span/button '
        self.driver.find_element_by_xpath(img_button1).click()
        # 调用AutoIt脚本实现文件上传
        os.system(r'D:\Python_work\AutoIt_Script\规格图片.exe')
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="minor-brand"]/div/div/div[1]').click()
        self.driver.find_element_by_xpath('//li[contains(text(),"富记")]').click()
        self.driver.find_element_by_id("minor-spec").send_keys("默认规格")
        self.driver.find_element_by_id("minor-description").send_keys("无")
        add2 = '//*[@id="root"]/section/main/div/div[2]/div[2]/div[2]/div/div/div/div/div/div[1]/table/tbody/tr/td[' \
               '5]/a[2] '
        self.driver.find_element_by_xpath(add2).click()
        sleep(0.5)
        # 返回
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[1]/div/div/div[2]/div/div[1]/div/button').click()
        # 查看已添加的辅料
        self.driver.find_element_by_xpath(food_key1).clear()
        self.driver.find_element_by_xpath(food_key1).send_keys("自动化测试")
        self.driver.find_element_by_xpath(food_search1).click()
        sleep(0.5)

        # 编辑
        editor1 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a[3]'
        self.driver.find_element_by_xpath(editor1).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="root"]/section/main/div/div[7]/div[2]/button[2]').click()

        # 关键字搜索
        self.driver.find_element_by_xpath(food_key1).clear()
        self.driver.find_element_by_xpath(food_key1).send_keys("自动化测试")
        self.driver.find_element_by_xpath(food_search1).click()
        sleep(0.5)
        # 规格详情
        sp_details1 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a[1]'
        self.driver.find_element_by_xpath(sp_details1).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[1]/div/div/div[2]/div/div[1]/div/button').click()

        # 关键字搜索
        self.driver.find_element_by_xpath(food_key1).clear()
        self.driver.find_element_by_xpath(food_key1).send_keys("自动化测试")
        self.driver.find_element_by_xpath(food_search1).click()
        sleep(0.5)
        # 辅料详情
        food_details1 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[' \
                        '6]/a[2] '
        self.driver.find_element_by_xpath(food_details1).click()
        sleep(0.5)
        self.driver.find_element_by_xpath(
            '//*[@id="root"]/section/main/div/div[1]/div/div/div[2]/div/div[1]/div/button').click()

        # 关键字搜索
        self.driver.find_element_by_xpath(food_key1).clear()
        self.driver.find_element_by_xpath(food_key1).send_keys("自动化测试")
        self.driver.find_element_by_xpath(food_search1).click()
        sleep(0.5)
        # 删除食材
        food_delete1 = '//*[@id="root"]/section/main/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[6]/a[4]'
        self.driver.find_element_by_xpath(food_delete1).click()
        sleep(0.5)

    def test_2_delete(self):
        start = datetime.datetime.now()
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
                self.driver.find_element_by_xpath(element).click()  # 删除 二次确认
            except Exception as error:
                print(error)
            else:
                print("辅料删除成功")
                end = datetime.datetime.now()
                print("test_2_delete 遍历耗时：", str(end-start))
                return element
        sleep(0.5)
        print("end:辅料库测试流程结束")

    def test_3_to_audit(self):
        """辅料库--待审核辅料库"""
        sleep(1)
        # 待审核辅料库
        to_audit1 = '//*[@id="root"]/section/main/div[1]/div/div[2]/div[1]/div/div/div/div/div[1]/div[2]/p'
        self.driver.find_element_by_xpath(to_audit1).click()
        sleep(0.5)
        # 通过申请
        allow1 = '//*[@id="root"]/section/main/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[7]/a[1]'
        self.driver.find_element_by_xpath(allow1).click()
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="keywords"]/div/div/ul/li/div/input').send_keys("大米")
        # 模拟键盘回车添加sku
        self.driver.find_element_by_xpath('//*[@id="keywords"]/div/div/ul/li/div/input').send_keys(Keys.ENTER)
        sleep(1)

    def test_4_save(self):
        start = datetime.datetime.now()
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[5]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        b = '/html/body/div[4]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        c = '/html/body/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        d = '/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        e = '/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        f = '/html/body/div[8]/div/div[2]/div/div[2]/div/div/div[2]/div[2]/button[2]'
        lists = [a, b, c, d, e, f]
        for element in lists:
            try:
                self.driver.find_element_by_xpath(element).click()  # 食材选择-保存按钮
            except Exception as error:
                print(error)
            else:
                end = datetime.datetime.now()
                print("辅料审核通过")
                print("test_4_save 遍历耗时：", str(end-start))
                return element

        # 拒绝申请
        sleep(1)
        refuse1 = '//*[@id="root"]/section/main/div[2]/div/div/div/div/div/div/div/table/tbody/tr[1]/td[7]/a[2]'
        self.driver.find_element_by_xpath(refuse1).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("replyContent").send_keys("自动化test-未上市")
        sleep(0.5)

    def test_5_send(self):
        start = datetime.datetime.now()
        print("遍历字典找到想要的元素定位")
        a = '/html/body/div[5]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        b = '/html/body/div[4]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        c = '/html/body/div[3]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        d = '/html/body/div[6]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        e = '/html/body/div[7]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        f = '/html/body/div[8]/div/div[2]/div/div[2]/div/p[2]/button[2]'
        lists = [a, b, c, d, e, f]
        for element in lists:
            try:
                self.driver.find_element_by_xpath(element).click()  # 审核不通过 发送按钮
            except Exception as error:
                print(error)
            else:
                end = datetime.datetime.now()
                print("辅料审核已拒绝")
                print("test_4_save 遍历耗时：", str(end - start))
                return element

            print("辅料库流程测试完成！")
            print("----------------------------------------------------------------------")

    @classmethod
    def tearDownClass(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.close()
        print("关闭浏览器")


if __name__ == '__main__':
    unittest.main()
