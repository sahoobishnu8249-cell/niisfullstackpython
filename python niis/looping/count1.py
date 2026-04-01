#WAP to initialize no 125 count no of odd and even gigit
no=125
oc,ec=0,0
while no!=0:
	r=no%10
	if r%2==0:
		ec=ec+1
	else:
		oc=oc+1
	no=no//10
print("no of odd digit=",oc)
print("no of even digit=",ec)
