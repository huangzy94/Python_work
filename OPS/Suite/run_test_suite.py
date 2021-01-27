import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from OPS.Suite.Email.AutoSendEmail import AutoSendEmail
from OPS.Log.log import PrintLog

"""
Created on 2020年4月
"""


class TestRunner:
    """测试集合"""

    def __init__(self, stream, verbosity, title, description, tester):
        self.stream = stream
        self.verbosity = verbosity
        self.title = title
        self.description = description
        self.tester = tester

    def discover(self):
        """执行测试套件"""
        # 定义测试目录为当前目录中的TestCase目录
        test_dir = r'D:\Python_work\OPS\TestCase'

        # pattern为根据测试目录查找所有包含test的测试用例,使用discover方法将多个测试用例添加到测试套件中执行
        suite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
        runner = HTMLTestRunner(self.stream,           # 输出报告路径
                                self.verbosity,        # 打印内容详细程度（2代表详细）
                                self.title,            # 标题
                                self.description,      # 描述
                                self.tester)           # 测试人员
        runner.run(suite)


if __name__ == '__main__':
    # %Y-%m-%d %H_%M_%S
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    print(now)
    # 打印日志
    logger = PrintLog()
    logger.debug("开始运行测试套件/集合：run_test_suite.py")
    # 定义报告文件的命名方式及存放路径
    # w 是写入模式
    # r 是读取模式
    # wb 是二进制写入
    filepath = "./Report/" + now + "_result.html"
    r = open(filepath, "wb")
    # 执行测试
    runner1 = TestRunner(r, 2, "UI自动化测试报告", "安品-运维中心", "HZY")
    runner1.discover()
    r.close()
    logger.debug("测试报告已生成,本地存放路径：" + r'D:\Python_work\OPS\Suite\Report')
    # 通过邮件发送测试报告
    s = AutoSendEmail("13683339705@163.com", "WTXRICRWULNRZYZG", 'smtp.163.com')
    s.Send(filepath)
    logger.debug("已发送测试报告")


