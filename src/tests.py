#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/6/1
# Time: 13:44
# from datetime import datetime
import logging
import logging.config
#
#
# def a():
#     pass
#
# x = a
# print type(x)
#
# n = datetime.now()
# print datetime.strftime(n, '%Y-%m-%d')
import threading

import datetime
import requests

# def hello():
#     def loop():
#         try:
#             a = 0
#         except requests.exceptions.ReadTimeout:
#             pass
#
#     t = threading.Thread(target=loop)
#     t.start()
# import schedule
# import time
#
#
# def hello(a):
#     print a
#
# schedule.every(2).seconds.do(hello, 'kk')
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)
from src import const
#
# logging.config.fileConfig(const.LOGGING_CONF)
# logger = logging.getLogger(__name__)
# logger.info('Hi, foo%s %s' % ('a', 'b'))

print datetime.datetime(map([2017, 1, 2], int))
