c=0
for i in range(4,0,-1):
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(0,c,1):
		print(end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	print()
	c=c+2