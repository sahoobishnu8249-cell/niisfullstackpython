c=1
for i in range(1,5,1):
	a=[]
	for j in range(i):
		a.append(c)
		c=c+1
	if i%2==0:
		a.reverse()
	for k in a:
		print(k,end=" ")
	print()