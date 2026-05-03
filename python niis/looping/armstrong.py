for no in range(1,1001,1):
	p=0
	temp=no
	while temp!=0:
		temp=temp//10
		p=p+1
	temp=no
	arm=0
	while temp!=0:
		r=temp%10
		arm=arm+r**p
		temp=temp//10
	if no==arm:
		print(no,"is armstrong number")
