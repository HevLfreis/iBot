#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/6/1
# Time: 9:44
import datetime

from const import *


def message(args):

    text = u""
    today = datetime.datetime.now()
    love = datetime.datetime.strptime(args['start_day'], '%Y-%m-%d')
    b_birth = datetime.datetime.strptime(args['b_birth'], '%Y-%m-%d')
    g_birth = datetime.datetime.strptime(args['g_birth'], '%Y-%m-%d')
    delta = (today-love).days

    if b_birth == today.date():
        text += u"今天是%s的生日\n" % B_NAME
    if g_birth == today.date():
        text += u"今天是%s的生日\n" % G_NAME

    if (delta + 2) % 100 == 0:
        text += u"后天是 %d 天纪念日\n" % (delta+2)
    elif delta % 100 == 0:
        text += u"今天是 %d 天纪念日\n" % delta

    text += u"我们在一起的第 %d 天" %delta
    return text


if __name__ == '__main__':
    print message({'start_day': '2017-03-12'})
