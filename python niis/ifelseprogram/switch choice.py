#WAP take two number from keyboard enter your choice 1.add 2.sub 3.mult
print("enter two number")
no1=int(input())
no2=int(input())
print("enter your choice\n1.add\n2.sub\n3.mult")
ch=int(input())
match ch:
      case 1:print("sum=",no1+no2)
      case 2:print("sub=",no1-no2)
      case 3:print("mult=",no1*no2)
      case _:print("invalid choice")