s=0
for no in range(10,21,1):
	d=2
	c=0
	while d<=no//2:
		if no%d==0:
			c=c+1
			break
		d=d+1
	if c==0:
		s=s+no
		print(no,"prime number")
print("sum=",s)
	