#!/usr/bin/env python
#coding:utf-8


# 运行时间:	27ms
# 内存占用:	2960KB

"""
# 思路一:
	计算n!末尾0的个数和n!有多少个因子与10有关;
	结果后面有0的无非就是2*5,4*5,6*5...或者2*10，2*20....
# 解法:
	找出2...n每个数拥有因子2的个数countTwo和拥有因子5的个数countFive，可与组成结尾为0的数，就是min{countTwo,countFive}；

"""
def getZero1(num):
	countTwo = 0
	countFive = 0
	if num == 1:
		return 0
	for item in range(2,num+1):
		while(item % 2 == 0):
			item = item/2
			countTwo += 1
		while(item % 5 == 0):
			item = item/5
			countFive += 1
	return countTwo if countTwo < countFive else countFive

"""
# 运行时间： 21ms
# 占用内存: 2952K

# 思路:
	- 求出n!的结果;
	- 将结果转化为字符串进行处理;
	- 逆序判断，依次判断n!的结果;
	- 如果为0，次数加1；如果不为0，直接退出;
"""
 
def getZero2(num):
	result = reduce(lambda x,y:x*y,range(1,num+1))
	result = str(result)
	result = result[::-1]
	count = 0 
	for item in result:
	    if item == '0':
	        count += 1
	    else:
	        break
	return count



if __name__ == "__main__":
    num = input()
    print getZero1(num)
    print getZero2(num)
    
    
