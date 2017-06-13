#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/6/1
# Time: 9:42
import os
import random
import re

import datetime
import requests
from bs4 import BeautifulSoup

from const import IMAGE_DIR, logger


def messages(args):
    folder = datetime.datetime.now().strftime('%Y-%m-%d')
    path = os.path.join(IMAGE_DIR, folder)
    pics = os.listdir(path)

    if len(pics) == 0:
        return os.path.join(IMAGE_DIR, 'default.jpg')

    for p in pics:
        if 'Lpip' in p:
            return os.path.join(path, p)

    return os.path.join(path, random.choice(pics))


def crawl_images(args):
    pc = PivixCrawler(args)
    pc.login()
    pc.run()


class PivixCrawler:

    LOGIN_PAGE = 'https://accounts.pixiv.net/login'
    LOGIN_URL = 'https://accounts.pixiv.net/api/login'
    RANK_URL = 'https://www.pixiv.net/ranking.php?mode=daily'
    ILLUSTRATION_URL = 'https://www.pixiv.net/member_illust.php'

    sess = requests.Session()

    def __init__(self, args, topN=10):
        self.timestamp = datetime.datetime.now()
        self.username = args['pivix_username']
        self.password = args['pivix_password']
        self.topN = topN

    def login(self):
        data = {
            'pixiv_id': self.username,
            'password': self.password,
            'post_key': '',
            'source': 'pc',
            'ref': 'wwwtop_accounts_index',
            'return_to': 'https://www.pixiv.net/'
        }

        home = self.sess.get(self.LOGIN_PAGE)
        post_key = re.findall('name="post_key"\svalue="(.*?)"', home.content)
        data['post_key'] = post_key[0]
        login = self.sess.post(url=self.LOGIN_URL, data=data)
        if login.status_code != 200:
            logger.debug('login to pivix failed')

    def run(self):
        rank = self.sess.get(self.RANK_URL)
        soup = BeautifulSoup(rank.content, 'html.parser', from_encoding='utf-8')

        ranking_items = soup.find_all('section',
                                      {'class': 'ranking-item'},
                                      limit=self.topN)

        for item in ranking_items:
            url = item.find('img')['data-src']
            url = re.sub(r'(c/|240x480/|_master1200)', '', url)
            url = url.replace('master', 'original')

            r = self.sess.get(url, headers={'Referer': self.ILLUSTRATION_URL})
            logger.info('access pivix url: %s status: %d' % (url, r.status_code))
            if r.status_code == 404:
                url = re.sub(r'jpg$', 'png', url)
                r = self.sess.get(url, headers={'Referer': self.ILLUSTRATION_URL})
                logger.info('retry access pivix url: %s status: %d' % (url, r.status_code))
            creator = re.sub(r'[^A-Za-z0-9]+', '', item['data-user-name'])
            file_name = item['data-id']+'-'+creator+'.'+url[-3:]
            self.save(file_name, r.content)

    def save(self, name, content):
        folder = self.timestamp.strftime('%Y-%m-%d')
        prefix = self.timestamp.strftime('%Y%m%d%H%m')
        path = os.path.join(IMAGE_DIR, folder)

        if not os.path.exists(path):
            os.mkdir(path)

        with open(os.path.join(path, prefix+'-'+name), 'wb') as f:
            f.write(content)

        logger.info('pivix file saved: %s %s' % (folder, name))

if __name__ == '__main__':
    pc = PivixCrawler({'pivix_username': 'freeeeeeeee', 'pivix_password': '021000920'})
    pc.login()
    pc.run()
    # print messages(1)