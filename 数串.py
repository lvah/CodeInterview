#!/usr/bin/env python
#coding:utf-8

num = input()
nums = raw_input().split()

# 高阶函数
li  = sorted(nums, lambda x, y : -cmp(x+y, y+x))
print ".".join(li)

