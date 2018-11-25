# coding:utf-8
__auth__ = 'Lu'
'''
description: 新闻内容页
'''
from src.common import base_page
from appium.webdriver.common import mobileby
from src.common import gesture_mainpulation
import time


class ContentPage(base_page.BasePage):

    by = mobileby.MobileBy()

    #pop_login_windows = (by.ID, "com.jifen.qukan:id/i4")
   # pop_login_ok = (by.ID, "com.jifen.qukan:id/i1")
    # 图片类型新闻
    type_news = {"photo_type_news":"com.jifen.qukan:id/i8","video_type_news":"com.jifen.qukan:id/agy","letter_type_news":"com.jifen.qukan:id/abi"}
    # 视频类型新闻
    #video_type_news = (by.ID, "")
    # 文字类型新闻
   # letter_type_news = (by.ID, "")

    # 判断登陆窗口是否弹出，若弹出则处理
    #def pop_login_window(self):
    #    self.pop_is_exist( self.pop_login_windows, self.pop_login_ok)

    # 判断新闻内容类型
    def judge_news_content_type(self):
        types = self.judge_views_content_type(self.type_news)
        return types

    # 向下滑动
    gesture_mainpulation = gesture_mainpulation.GestureMainpulation()

    # 向左滑动页面
    def swipe_right(self):
        self.gesture_mainpulation.swipe_right(self.driver)

    def swipe_left(self):
        self.gesture_mainpulation.swipe_left(self.driver)
        time.sleep(10)
        self.gesture_mainpulation.swipe_right(self.driver)

    # 向下滑动页面
    def swipe_down(self):
        self.gesture_mainpulation.swipe_down(self.driver)
        time.sleep(8)
        self.gesture_mainpulation.swipe_up(self.driver)

