# coding:utf-8
__author__ = 'Helen'
'''
description:UI页面公共类
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from log import Logger
from config.globalparameter import home_page_receive

mylog = Logger.Logger("base_page").getlog()

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.mylog = mylog

    def find_element(self, unlock_read, available_get):
        # 重写find_element方法，显式等待
        try:
            WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(unlock_read))
            element = self.driver.find_element_by_id(available_get[1])
            if element.__getattribute__("text") == home_page_receive:
                if ec.element_to_be_clickable(unlock_read):
                  return self.driver.find_element(unlock_read)
                else:
                  self.mylog.error(u'元素不可点击')
            else:
                self.mylog.warning(u"已领取时段奖励")
        except Exception as e:
            raise e

    def find_element_by_xpath(self, *loc):
        try:
            return WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(loc))
        except Exception as e:
            raise e

    def pop_is_exist(self, pop_login_window, pop_login_ok):
        try:
            WebDriverWait(self.driver, 15).until(ec.visibility_of(pop_login_window))
            if ec.element_to_be_clickable(pop_login_ok):
                return self.driver.find_element(pop_login_ok)
            else:
                self.mylog.warning(u"登陆按钮未找到")
        except Exception as e:
            raise e

    def judge_views_content_type(self, type_news):
        news_type = ""
            #news_type = ""
        for key in type_news.keys():
            try:
                element = self.driver.find_element_by_id(type_news[key])
                element.__getattribute__("id")
                news_type = key
                break
            except Exception as e:
                e.message
                continue
        return news_type

    def send_keys(self, value, *loc):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError, e:
            raise e

    def element_is_exist(self, *loc):
        try:
            WebDriverWait(self.driver, 15).until(self.driver.find_element_by_id(*loc))
            return True
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False
