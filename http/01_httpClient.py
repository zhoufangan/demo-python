#!C:/Program Files/Python36
# -*- coding: utf-8 -*-

# http.client 对应python2.X 的 httplib 模块。
# 该库一般不直接使用，比较底层。

import http.client


# GET的官方例子：
def get():
    # 创建Connection对象
    conn = http.client.HTTPSConnection("www.baidu.com")
    conn.request("GET", "/index.html", "", {})
    res = conn.getresponse()
    print(res.status, res.reason, res.info())


def post():
	# 创建Connection对象
	conn = http.client.HTTPSConnection("www.qidian.com")
	conn = request("POST", "/index.html", "", {})
	res = conn.getresponse()
	print(res.status, res.reason, res.info())

get()

# post()
