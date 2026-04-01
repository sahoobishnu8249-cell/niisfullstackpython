s="1598"
for i in range(len(s)-1,-1,-1):
	for j in range(0,i+1,1):
		print(s[j],end="")
	print()