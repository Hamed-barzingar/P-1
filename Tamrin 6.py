a = input('Enter your namber : ')
b = input('Enter your nameb for cerch : ')
c = len(a)
n = 0
g = 0

while n < c :
	if b in a[g] :
		print (a[g] , end = ' ')
		g += 1
		n += 1
	else :
		g += 1
		n += 1