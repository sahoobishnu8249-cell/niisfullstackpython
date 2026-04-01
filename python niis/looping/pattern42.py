for i in range(1,5,1):
	for j in range(1,i+1,1):
		if i%2==0:
			print("#",end="")
		else:
			print("@",end="")
	print()