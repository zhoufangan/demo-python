#!/usr/bin/python3

# Python3 默认情况下 源文件以UTF-8格式编码。所有字符串都是 unicode 字符串。
# 也可以指定字符串

# -*- coding: UTF-8 -*-

# 标识符
# 首字母 字母或者_
# 字母、数字、_
# 标识符对大小写敏感

import keyword

print(keyword.kwlist)

# python以缩进标识一个代码块,没有{}哦,
# 若同一个代码块缩进不一致，会导致错误哦
a = 10 * 10

if (a > 100):
    print("a大于100")
elif (a == 100):
    print("a等于100")
else:
    b = a
    print("a小于100")
    print(b == a)

# 字符串
# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
# python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
# 字符串是不可变的。

word = '字符串'
sentence = "这是一个句子。"
paragraph = """三引号字符串，可以存在多行这是一个段落，
可以由多行组成"""
print(word)
print(sentence)
print(paragraph)
