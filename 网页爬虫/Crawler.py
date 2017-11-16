#!/usr/bin/python
# -*- coding:utf-8 -*-

# urllib模块提供了读取web页面的接口
# re模块 正则表达式

import sys
import urllib.request
import urllib.response
import re


def getHtml(url):
    response = urllib.request.urlopen(url)
    page = response.read()
    print("返回结果", page)


getHtml("http://www.cnblogs.com/sysu-blackbear/p/3629420.html")
