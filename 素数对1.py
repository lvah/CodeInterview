#!/usr/bin/env python
#coding:utf-8


# 判断是否为质数(素数)；
def isprime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


num = input()
# 列表存储0-num之间存在的所有素数；
primeL = []
# 列表存储0-num中，和为num的所有质数对;eg:[(5,5),(3,7)].
doublePrime = []

# 存储所有的质数到primeL列表中;
for i in range(2,num):
    if isprime(i):
        primeL.append(i)

        
 # 存储所有的质数对到doublePrime列表中;
 # 思路:
 #      分别遍历所有的质数的组合;
 #      判断，如果和为num，则存储;
for i in range(0,len(primeL)):
    for j in range(i,len(primeL)):
        if primeL[i]+primeL[j] == num:
            doublePrime.append((primeL[i],primeL[j]))

# 打印存储质数对的列表长度，也就是质数对的个数;        
print len(doublePrime)    
  
