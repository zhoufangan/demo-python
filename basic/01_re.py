#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import re


# compile编译函数 match匹配函数
# [0,3）[3,6） (36,+)
# (0,40]  (80,160]  (160,+) [200,+ )
# [0,1000) [100000,200000)

# 无限的
# (0,+)
# [0,+)
# 有限的
# (0,1000)
# [0,1000)
# (0,1000]
# [0,1000]

def hello():
    m = re.match("[\(\[](\d+)\,(\+|\d+)[\)\]]", "[0,+)")

    # 无限的
    m1 = re.match('\((\d+)\,(\+)\)', '(0,+)')
    m2 = re.match('\[(\d+)\,(\+)\)', '[0,+)')
    # 有限的
    m3 = re.match('\((\d+)\,(\d+)\)', '(0,1000)')
    m4 = re.match('\[(\d+)\,(\d+)\)', '[0,1000)')
    m5 = re.match('\((\d+)\,(\d+)\]', '(0,1000]')
    m6 = re.match('\[(\d+)\,(\d+)\]', '[0,1000]')

    print(m1 == None)
    print(m2 == None)
    print(m3 == None)
    print(m4 == None)
    print(m5 == None)
    print(m6 == None)

    # m是对象,不匹配返回空值
    if (m != None):
        min = m.group(1)
        max = m.group(2)
        print('m1', min, max)
    else:
        print('m1不匹配')


        # m1 = re.match('\((\d+)\,(\+)\)', '(0,+)')
        # m2 = re.match('\((\d+)\,(\d+)\)', '(0,1000)')
        # m3 = re.match('\[(\d+)\,(\d+)\)', '[0,1000)')
        # m4 = re.match('\[(\d+)\,(\+)\)', '[0,+)')


hello()
