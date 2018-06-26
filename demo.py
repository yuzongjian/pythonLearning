#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2018/6/25 23:41
#@Author: yuzongjian
#@File  : demo.py
name = input("Please input your name:")
# 打印输出有下面三种方法，最常用的是第一种
print("hello {0}".format(name))
print("hello" + name)
print("hello %s" %name)
print("1213"+"100")
classmates = ['123','1123']
print(classmates.__len__())
for name in classmates:
    print(name)
    d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    print(d['Michael'])
    print(d.get('Thomas'))