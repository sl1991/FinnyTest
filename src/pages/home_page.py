# coding:utf-8
__auth__ = 'Lu'
'''
description: 推荐页
'''
from src.common import base_page
from appium.webdriver.common import mobileby


class HomePage(base_page.BasePage):

    by = mobileby.MobileBy()
    # 领取红包弹出框
    # new_person_package = (by.ACCESSIBILITY_ID, "com.jifen.qukan:id/a4y")
    # 领取按钮
    unlock_read = (by.ID, "com.jifen.qukan:id/ul")
    available_get = (by.ID, "com.jifen.qukan:id/um")
    content_first = (by.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout")

    # etUser_loc = (by.CLASS_NAME, "android.widgetLinearLayout")
    # def click_btn_login(self):
        # if self.element_is_exist(*self.new_person_package):
           # self.find_element(*self.new_person_package).click()
    # 点击领取金币按钮
    def click_unlock_close(self):
        self.find_element(self.unlock_read, self.available_get)

    # 点击某一个新闻内容
    def click_content_first(self):
        ele = self.find_element_by_xpath(*self.content_first)
        self.mylog.warning(u'准备点击')
        ele.click()
        self.mylog.warning(u'已经点击')
