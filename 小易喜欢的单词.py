#!/usr/bin/env python
#coding:utf-8



# 条件1：判断字符串是否均为大写字母;
def condition1(s):
    return s.isupper()
      
# 条件2:判断字符串中是否有连续相等的字母;   
def condition2(s):
    for i in range(0,len(s)-1):
        if s[i] == s[i+1]:
            return False
    return True

# 条件3：判断是否有“xyxy”这样的子序列
# 思路:
#       1). 先删除字符串中不重复的元素;
#       2). 将剩余的元素进行组合，判断这些组合是否有重复的内容;    


def main():
    s = raw_input()
    if condition1(s) and condition2(s):
        print "Likes"
    else:
        print "Dislikes"
    
main()
