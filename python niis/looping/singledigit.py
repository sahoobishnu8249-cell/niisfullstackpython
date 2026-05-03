no=2457
while no>9:
	s=0
	while no>0:
		r=no%10
		s=s+r
		no=no//10
	no=s
print(no)