# statement 3 factorial no.
def facttest():
	print("enter a no")
	no=int(input())
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
result=facttest()
print("factorial is:",result)