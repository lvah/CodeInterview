def isprime(num):
	for i in range(2,num):
		if num % i == 0:
			return False
	return True



num = input()
L = []
doubleL = []
for i in range(2,num):
	if isprime(i):
		L.append(i)
print L
for i in L:
	j = num - i
	if isprime(j) and i <= j :
		doubleL.append((i,j))

print doubleL
print len(doubleL)
