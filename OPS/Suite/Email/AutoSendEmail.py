import yagmail
import time


class AutoSendEmail:
    def __init__(self, user, password, host):
        self.user = user
        self.password = password
        self.host = host

    def SMTP(self):
        return yagmail.SMTP(user=self.user,  # 邮箱账户
                            password=self.password,  # smtp服务授权码
                            host=self.host)  # smtp服务器地址

    def Send(self, filepath):
        t = AutoSendEmail.SMTP(self)
        now = time.strftime("%Y-%m-%d %H")
        subject = 'OPS-UI 自动化测试报告'
        contents = [now, 'This is UI Automated test report', "安品-运维中心"]

        t.send(to="huangzy94@dingtalk.com",  # 接收人，如果是多个收件人的话，写成list
               cc="13683339705@163.com",  # 抄送人
               subject=subject,  # 标题
               contents=contents,  # 邮件正文
               attachments=[filepath])  # 附件


if __name__ == '__main__':
    # 通过邮件发送测试报告
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filepath = "./Report/" + now + "_result.html"
    s = AutoSendEmail("13683339705@163.com", "WTXRICRWULNRZYZG", 'smtp.163.com')
    s.Send(filepath)
