#WAP to calculate the number is even or odd
print("enter a number")
num=int(input())
print("1.check even")
print("2.check odd")
choice=int(input("enter your choice:"))
match choice:
    case 1:
      if num%2==0:
        print("even number")
      else:
        print("not even")
    case 2:
      if num%2!=0:
      	print("odd number")
      else:
      	print("not odd")
    case _:
    	print("invalid choice")