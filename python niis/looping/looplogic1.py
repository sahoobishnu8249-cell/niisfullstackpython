#WAP initialize no 125 sum of digit
no=125
s=0
while no!=0:
	r=no%10
	s=r+s
	no=no//10
print("sum of digit=",s)