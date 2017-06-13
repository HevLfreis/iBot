#!/usr/bin/env python
# coding: utf-8
# created by hevlhayt@foxmail.com 
# Date: 2017/6/2
# Time: 14:56
import os
import logging.config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGGING_CONF = os.path.join(BASE_DIR, 'src/logging.conf')
IMAGE_DIR = os.path.join(BASE_DIR, 'images')

B_NAME, G_NAME = '', ''

logging.config.fileConfig(LOGGING_CONF)
logger = logging.getLogger(__name__)
