
a=0
b=1
print(a,b,end="\t")
r=8
while r>2:
	c=a+b
	print(c,end="\t")
	a=b
	b=c
	r=r-1