# statement 4 evenodd program.
def check(no):
	if no%2==0:
		return "even number"
	else:
	    return "odd number"
print("enter a number")
no=int(input())
print(check(no))