# statement 4 factorial no.
def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
print("enter a number")
no=int(input())
result=facttest(no)
print("factorial is",result)