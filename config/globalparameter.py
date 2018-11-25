# coding:utf-8
__authot__ = 'Lu'
'''
description: global configuration
'''
import time
import os

# 获取项目路径
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# 测试用例代码存放路径（用于构建suit,注意该文件夹下的文件都应该以test开头命名）
test_case_path = project_path + "\\src\\test_case"
# print u'日志路径：' + log_path
log_path = project_path + "\\src\\logs\\"
# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path + "\\report\\"
report_name = report_path + time.strftime('%Y%m%d%H%S', time.localtime())
# 设置发送测试报告的公共邮箱、用户名和密码
smtp_server = 'smtp.qq.com'
email_name = "506443748@qq.com"
email_password = "ugmlugccnvrgbjif"
email_To = "506443748@qq.com"

# platform
platformName = 'Android'
platformVersion = '8.1.0'
# app
appActivity = 'com.jifen.qkbase.start.JumpActivity'
appPackage = 'com.jifen.qukan'
deviceName = '9YEDU18928010522'
automationName = 'uiautomator2'

# app content
home_page_receive = '领取'
photo_type_news = "photo_type_news"
video_type_news = "video_type_news"
letter_type_news = "letter_type_news"
