t = print ('hello wellcom to this game')
m =print ('1 : stone _ 2 : paper _ 3 : scissor')

a = 0
b = 1

while True :
	while True :
		c1= int(input('Enter your namber : '))
		c2 = int(input('Enter your namber : '))
		if c1== 1 and c2== 2 :
			print ('win c2')
		if c1 == 1 and c2 == 3 :
			print ('win c1')
		if c1 == 2 and c2 == 3 :
			print('win c2')
		if c2== 1 and c1== 2 :
			print ('win c1')
		if c2 == 1 and c1 == 3 :
			print ('win c2')
		if c2 == 2 and c1 == 3:
			print('win c1')
		b += 1
	b = 0		
	a += 1