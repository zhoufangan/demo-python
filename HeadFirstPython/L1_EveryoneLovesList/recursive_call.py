#!/usr/bin/python3
# -*- coding: UTF-8 -*-

movies = ["0", "0", "0", ["1", "1", "1", ["2", "2", "2", ["3", "3", "3", "3"]]]]

# 层次变量定义 最上层不空格
line = "----"


# 打印列表中的元素 并要标明层次
def recursive_call(datas, level):
    if (None == datas):
        return
    prefix = None
    if (0 == level):
        prefix = ""
    else:
        prefix = line * level

    length = len(datas)
    index = 0
    while (index < length):
        item = datas[index]
        if (isinstance(item, list)):
            recursive_call(item, level + 1)
        else:
            print(prefix + str(item))

        index += 1


recursive_call(movies, 0)
