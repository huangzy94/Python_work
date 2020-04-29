from selenium import webdriver
from OPS.Log.log import PrintLog
from time import *
import selenium

# 打印当前时间
print(ctime())


# 创建登录类，并定义初始化方法
class Login_first:
    def __init__(self, Username, Password, VcCode, Url):
        self.Username = str(Username)
        self.Password = str(Password)
        self.VcCode = str(VcCode)
        self.Url = str(Url)

    # 固定地址的简单写法
    # def URL1(Url):
    #     return "http://ap-"+Url+".td.com"
    # 定义地址的方法
    def URL(self):
        ops = "http://ap-ops.td.com"
        catering = "http://ap-catering.td.com"
        superior = "http://ap-superior.td.com"
        supplier = "http://ap-supplier.td.com"

        if self.Url == "ops":
            url = ops
        elif self.Url == "catering":
            url = catering
        elif self.Url == "superior":
            url = superior
        elif self.Url == "supplier":
            url = supplier
        else:
            url = self.Url
        # jenkins部署项目出现fix cannot find Chrome binary时，需要在Chrome后面加上执行程序的安装路径
        options = selenium.webdriver.ChromeOptions()
        options.binary_location = "C:\\Users\\hzy\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
        driver = selenium.webdriver.Chrome(chrome_options=options)
        # driver = webdriver.Chrome("C:\\Users\\hzy\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
        driver.get(url)
        print("当前访问地址为：%r" % url)
        logger = PrintLog()
        # 使窗口最大化
        driver.maximize_window()
        logger.debug("当前访问地址为：%r" % url)
        return driver

    # 定义登录方法
    def login(self):
        driver = Login_first.URL(self)
        driver.find_element_by_id("username").send_keys(self.Username)
        driver.find_element_by_id("password").send_keys(self.Password)
        driver.find_element_by_id("vcCode").send_keys(self.VcCode)
        driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/form/div[4]/div/div/span/button').click()
        driver.implicitly_wait(10)
        return driver


if __name__ == '__main__':
    t = Login_first("jgzh01", "su123456", "801B", "ops")
    t.login()
