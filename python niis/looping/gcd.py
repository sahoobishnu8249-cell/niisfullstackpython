no1=14
no2=12
if no1>=no2:
	n=no1
	d=no2
else:
	n=no2
	d=no1
r=n%d
while r!=0:
	n=d
	d=r
	r=n%d
print("gcd=",d)
print("lcm=",no1*no2//d)