a = int(input("Enter number of  rows"))
b=0
b = a+1
for i in range (1,b):
	for j in range (1 , b-i):
		print (" " , end=' ' )
	for k in range (1,i+1):
		print ( k , end=' ')
	for l in range (k-1,0, -1):
		print (l , end = ' ')
	
	print ()