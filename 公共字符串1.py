#!/usr/bin/env python
#coding:utf-8

# 第一种方法:

s1 = raw_input()
s2 = raw_input()

# 定义空字符串
resultStr = ""


for i in s1:            # 遍历s1字符串;
    if i not in s2:     # 判断i是否为s2的子字符;
            resultStr += i       

print resultStr            

