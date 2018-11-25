# coding:utf-8
__author__ = 'Lu'
'''
description: 邮件发送最新的测试报告
'''
import os
import smtplib
import os.path
from config import globalparameter as gl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from log import Logger

mylog = Logger.Logger("").getlog()

class SendEmail:

    def __init__(self):
        self.mylog = mylog

    # 定义邮件内容
    def email_init(self, report, report_name):
        with open(report, 'rb')as f:
            mail_body = f.read()

        # 创建一个带附件的邮件实例
        msg = MIMEMultipart()
        # 以测试报告作为邮件正文
        msg.attach(MIMEText(mail_body, 'html', 'utf-8'))
        report_file = MIMEText(mail_body, 'html', 'utf-8')
        # 定义附件名称（附件的名称随便定义）
        report_file["Content-Disposition"] = 'attachment;filename=' + report_name
        msg.attach(report_file)
        msg['Subject'] = '趣头条自动化测试报告：' + report_name
        msg['From'] = gl.email_name
        msg['To'] = gl.email_To
        try:
            server = smtplib.SMTP_SSL(gl.smtp_server, 465)
            server.login(gl.email_name, gl.email_password)
            server.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())
            server.quit()
        except smtplib.SMTPException:
            self.mylog.error(u'邮件发送测试报告失败 at ' + __file__)

    def send_report(self):
        # 找到最新的测试报告
        report_list = os.listdir(gl.report_path)
        report_list.sort(key=lambda fn: os.path.getmtime(gl.report_path + fn) if not os.path.isdir(gl.report_path + fn) else 0)
        new_report = os.path.join(gl.report_path, report_list[-1])
        # 发送邮件
        self.email_init(new_report, report_list[-1])
