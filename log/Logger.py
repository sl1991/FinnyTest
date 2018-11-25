# coding:utf-8
__author__ = 'Lu'
'''
description: log类
'''
import logging
import time
from config.globalparameter import log_path


class Logger(object):

    def __init__(self, logger):
        # 指定保存日志的文件路径，日志级别以及调用文件.将日志存入到指定的文件中
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # rq = time.strftime('%Y%m%d%H%m', time.localtime(time.time()))

        # 创建一个handler,用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_", time.localtime(time.time()))
        self.log_path = log_path
        self.log_name = self.log_path + self.log_time + 'test.log'

        fh = logging.FileHandler(self.log_name)
        fh.setLevel(logging.INFO)

        # 再创建一个handler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

        # 添加下面一句，在记录日志之后移除句柄
        #self.logger.removeHandler(ch)
        #self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()
        ch.close()

    def getlog(self):
        return self.logger
