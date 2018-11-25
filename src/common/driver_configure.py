# coding:utf-8
__authot__ = 'Lu'
'''
description: driver 配置
'''
from appium import webdriver
from config.globalparameter import platformName
from config.globalparameter import platformVersion
from config.globalparameter import appPackage
from config.globalparameter import appActivity
from config.globalparameter import deviceName
from config.globalparameter import automationName


class DriverConfig:

    def __init__(self):
        self.platformName = platformName
        self.platformVersion = platformVersion
        self.appPackage = appPackage
        self.appActivity = appActivity
        self.deviceName = deviceName
        self.automationName = automationName
        self.driver = webdriver
        self.desired_caps = {}

    def get_driver(self):
        try:
            self.desired_caps['platformName'] = self.platformName
            self.desired_caps['platformVersion'] = self.platformVersion
            self.desired_caps['appPackage'] = self.appPackage
            self.desired_caps['appActivity'] = self.appActivity
            self.desired_caps['unicodeKeyboard'] = True
            self.desired_caps['resetKeyboard'] = True
            self.desired_caps['newCommandTimeout'] = 6000
            self.desired_caps['noReset'] = True
            self.desired_caps['deviceName'] = self.deviceName
            self.desired_caps['automationName'] = self.automationName

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_caps)

            return self.driver
        except Exception, e:
            raise e
