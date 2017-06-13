#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/6/1
# Time: 9:45
import random

import requests
from bs4 import BeautifulSoup

from const import logger

MUSIC_URL = 'http://music.163.com/song/'
MUSIC_LIST_API = 'http://music.163.com/api/playlist/detail?id='


class MusicRecommender:

    b_id, g_id = '', ''
    b_music_set, g_music_set = set(), set()
    info_map = {}

    def __init__(self, args):
        self.b_id = args['music_b_id']
        self.g_id = args['music_g_id']
        self.get_list()

    def get_list(self):
        self.b_music_set, self.g_music_set = set(), set()

        r = requests.get(MUSIC_LIST_API + self.b_id).json()

        for track in r['result']['tracks']:
            self.b_music_set.add(track['id'])
            self.info_map[track['id']] = '['+track['artists'][0]['name']+'] '+track['name']

        r = requests.get(MUSIC_LIST_API + self.g_id).json()
        for track in r['result']['tracks']:
            self.g_music_set.add(track['id'])
            self.info_map[track['id']] = '['+track['artists'][0]['name']+'] '+track['name']

        logger.info('music list len: %d %d' % (len(self.b_music_set), len(self.g_music_set)))

    def recommend(self):
        old_b_set = set(self.b_music_set)
        old_g_set = set(self.g_music_set)

        self.get_list()

        b_diff = self.b_music_set - old_b_set
        g_diff = self.g_music_set - old_g_set

        if len(b_diff) == 0:
            b_rec_id = random.choice(list(self.b_music_set))
        else:
            b_rec_id = random.choice(list(b_diff))
        b_rec_text = self.info_map[b_rec_id] + ' \n' + MUSIC_URL + str(b_rec_id)

        if len(g_diff) == 0:
            g_rec_id = random.choice(list(self.g_music_set))
        else:
            g_rec_id = random.choice(list(g_diff))
        g_rec_text = self.info_map[g_rec_id] + ' \n' + MUSIC_URL + str(g_rec_id)

        logger.info('recommend music: %d %d' % (b_rec_id, g_rec_id))
        return b_rec_text+'\n'+g_rec_text


def messages(rec):
    return rec.recommend()


if __name__ == '__main__':
    mr = MusicRecommender({'music_m_id': '60660461', 'music_f_id': '80050525'})
    mr.get_list()
    print mr.recommend()




