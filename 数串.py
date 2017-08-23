
num = input()
nums = raw_input().split()
print ''.join(sorted(nums, lambda x, y : -cmp(x+y, y+x)))

