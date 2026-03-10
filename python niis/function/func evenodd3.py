# statement 3 evenodd program.
def check():
	print("enter a number:")
	no=int(input())
	if no%2==0:
		return True
	else:
		return False
if check():
	print("even number")
else:
	print("odd number")