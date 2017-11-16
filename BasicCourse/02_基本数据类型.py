#!C:/Users/zhoufangan/AppData/Local/Programs/Python/Python36/
# -*- coding: utf-8 -*-

# 类型判断 Python还有继承呀
# 1.isinstance(a, int)      isinstance()会认为子类是一种父类类型。
# 2.type(A()) == A          type()不会认为子类是一种父类类型。

# list
def printList():
    l = []
    l.append(0)
    l.append(0)
    l.append(0)
    l.append(0)
    l.append(0)
    print(l)


# Tuple元组, 元素不可变, 但是内部可包含可变的对象,入list
def printTuple():
    t = ('abcd', 786, 2.23, 'runoob', 70.2)
    for x in t:
        print(x)


# Set集合 集合set 是一个无序不重复元素的序列。
def printSet():
    s = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
    for x in s:
        print(x)


def printDictionary():
    dict = {}
    dict['one'] = "1 - 菜鸟教程"
    dict[2] = "2 - 菜鸟工具"
    print(dict)


# printList()
# printTuple()
# printSet()
printDictionary()
