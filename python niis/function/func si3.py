#WAP to calculate simple intereast statement 3.
def sical():
	print("enter principal")
	P=float(input())
	print("enter rate")
	R=float(input())
	print("enter time")
	T=float(input())
	SI=(P*R*T)/100
	return SI
result=sical()
print("simple interest is:",result)
