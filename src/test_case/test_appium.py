# coding:utf-8
__auth__ = 'Lu'
'''
description: 测试推荐页
'''
import unittest
from src.pages import home_page, content_page
from src.common import gesture_mainpulation
from src.common import driver_configure
from config import globalparameter
import logging
import time


class TestAppium(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dconfigur = driver_configure.DriverConfig()
        cls.driver = dconfigur.get_driver()
        cls.GM = gesture_mainpulation.GestureMainpulation()

    def test_01(self):
        logging.warning(u"进入推荐页面")
        self.home_page = home_page.HomePage(self.driver)
        # 点击领取按钮
        self.home_page.click_unlock_close()
        # 点击第一条内容
        self.home_page.click_content_first()

    def test_02(self):
        logging.warning(u'进入具体新闻内容页面')
        self.content_page = content_page.ContentPage(self.driver)
        time.sleep(5)
        self.content_page.mylog.__setattr__("name","content_page")
        news_type = self.content_page.judge_news_content_type()
        if news_type == "":
            logging.warning(u"null")

        if news_type == globalparameter.photo_type_news:
            logging.warning(u"图片类型新闻")
            time.sleep(3)
            self.content_page.swipe_left()
        elif news_type == globalparameter.video_type_news:
            logging.warning(u"视频类型新闻")
        elif news_type == globalparameter.letter_type_news:
            logging.warning(u"文字类型新闻")
            self.content_page.swipe_down()
        else:
            logging.warning(news_type)

        # 判断是否有登陆的弹出框
        # flag = self.content_page.pop_is_exist()
        # if flag:
        #    logging.warning(u'存在登陆弹出框')
        # else:
        #    logging.warning(u'不存在登陆弹出框')

        #self.content_page.swipe_down()

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        logging.warning(u"测试完成")

    if __name__ == '__main__':
        unittest.main()
