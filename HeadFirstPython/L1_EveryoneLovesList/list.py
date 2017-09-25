#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import re

movies = ["Spider Man", "War for the Planet of the Apes III", "Wolf Warriors II"]


# 列表是否包含元素
def listContains(list, item):
    if (None == list):
        return False
    for x in list:
        if (x == item):
            return True


print(movies)
# 计算列表长度 len()
print(len(movies))
# 末尾添加数据 append
movies.append("变形金刚3")
print(movies)
# 末尾删除数据 pop() 不给值是自后一个 返回被删除的值
item = movies.pop()
print(movies)
movies.append(item)
# 删除指定数据 返回被删除的值
item = movies.pop(0)
print(movies)
# 指定位置添加数据 insert
movies.insert(0, item)
print(movies)
# 删除指定位置的元素
item = "变形金刚3"
movies.remove(item)
print(movies)
movies.append(item)
