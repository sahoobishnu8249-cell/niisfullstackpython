#statement 3 add 2 no.
def add():
	print("enter a number")
	no1=int(input())
	print("enter another number")
	no2=int(input())
	s=no1+no2
	return s
res=add()
print("sum=",res)