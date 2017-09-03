s = raw_input()
sL = len(s)


if sL < 6:
	print s
elif  6 < sL <= 14:
	print s[:6],s[6:]
else:
	print s[:6],s[6:14],s[14:]
