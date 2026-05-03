for no in range(1,1001,1):
	d=1
	sum=0
	while d<=no//2:
		if no%d==0:
			sum=sum+d
		d=d+1
	if sum==no:
		print(no,"perfect number")