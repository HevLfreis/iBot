#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/6/1
# Time: 9:42
import argparse

import itchat
import schedule
import time

from const import *
import daydream
import pivix
import weather
import music

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--conf",
                    nargs="?",
                    type=str,
                    const='ibot.conf',
                    default='ibot.conf')
conf = parser.parse_args()

###############################################################
# parse conf
args = {}
with open(conf.conf, 'r') as f:
    for line in f:
        k, v = line.strip().split('=')
        args[k.lower()] = v

B_NAME = args['b_name']
G_NAME = args['g_name']

###############################################################
# start wechat
logger.info('starting wechat')
itchat.auto_login(enableCmdQR=2, hotReload=True)
friends = itchat.search_chatrooms(name='SH')
darling = friends[0].UserName
mps = itchat.search_mps(name=u'中国联通')
ticker = mps[0].UserName

logger.info('wechat online, waiting for flows')

MR = music.MusicRecommender(args)


def flow():
    logger.info('start flowing ...')
    dm = daydream.message(args)
    wm = weather.message(args)
    pm = pivix.messages(args)
    mm = music.messages(MR)
    itchat.send(dm, toUserName=darling)
    itchat.send(wm, toUserName=darling)
    itchat.send_image(pm, toUserName=darling)
    itchat.send(mm, toUserName=darling)


def keep_alive():
    # print 'keep alive with mps ...'
    itchat.send('bon', toUserName=ticker)


pivix.crawl_images(args)
flow()
schedule.every(8).seconds.do(keep_alive)
schedule.every().day.at("03:30").do(pivix.crawl_images, args)
schedule.every().day.at("08:10").do(flow)

while True:
    schedule.run_pending()
    time.sleep(1)
