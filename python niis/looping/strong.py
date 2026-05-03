for no in range(1,100001,1):
	temp=no
	str=0
	while temp>0:
		r=temp%10
		f=1
		while r>0:
			f=f*r
			r=r-1
		str=str+f
		temp=temp//10
	if no==str:
		print(no,"is strong number")
	
