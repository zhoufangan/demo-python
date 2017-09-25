#!/usr/bin/python3
# -*- coding: UTF-8 -*-

movies = ["Spider Man", "War for the Planet of the Apes III", "Wolf Warriors II"]


# exercise1 向每个电影元素中,添加年份
def addYear(list):
    ms = []
    length = len(list)
    i = 0
    while i < length:
        ms.append(list[i])
        ms.append(2017)
        i += 1
    return ms


print(addYear(movies))
