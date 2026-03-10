# statement 4 simple interest.
def sical(P,R,T):
	SI=(P*R*T)/100
	return SI
print("enter principal")
P=float(input())
print("enter rate")
R=float(input())
print("enter time")
T=float(input())
result=sical(P,R,T)
print("simple interest is:",result)
