#WAP to initialize no 125 sum of odd and even digit
no=125
os,es=0,0
while no!=0:
	r=no%10
	if r%2==0:
		es=es+r
	else:
		os=os+r
	no=no//10
print("sum of odd digit=",os)
print("sum of even digit=",es)
