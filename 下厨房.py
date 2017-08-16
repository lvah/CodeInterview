#!/usr/bin/env python
#coding:-*- utf-8 -*-
"""
Name: 下厨房.py
Date: 2017-08-16
Author: lvah
Desc:

- 题目描述:
    牛牛想尝试一些新的料理，每个料理需要一些不同的材料，问完成所有的料理需要准备多少种不同的材料。

输入描述:
    每个输入包含 1 个测试用例。每个测试用例的第 i 行，表示完成第 i 件料理需要哪些材料，各个材料用空格隔开，输入只包含大写英文字母和空格，输入文件不超过 50 行，每一行不超过 50 个字符

输出描述:
    输出一行一个数字表示完成所有料理需要多少种不同的材料。

示例1:
```
    输入:
	BUTTER FLOUR
	HONEY FLOUR EGG
    输出:
	4
```
"""

import sys


def main(): 
    # 定义一个空列表，记录所有料理包含的所有材料；
    need = [] # 依次读取系统输入;
     
    # 此处没有用raw_input，是因为只能输入一行，换行，程序就结束;
    # sys.stdin想要结束输入，直接用ctrl+d;
    for line in sys.stdin:
        needline = line.split()
        need.extend(needline)
     
     
    # 通过将列表格式转换为集合格式，去除列表中重复的元素；
    lastNeed = set(need)
     
    # 使用python内置函数len(),得到需要材料的个数；
    return  len(lastNeed)

if __name__ == "__main__":
	print main()

