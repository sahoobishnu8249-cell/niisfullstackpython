c=0
for i in range(68,64,-1):
	for j in range(65,i+1,1):
		print(chr(j),end="")
	for j in range(0,c,1):
		print(end=" ")
	for j in range(i,64,-1):
		print(chr(j),end="")
	c=c+2
	print()

