#WAP take no from keyboard is divisible by 5 and 7 only 5 only 7 not divisible 5 and 7
print("enter a number")
no=int(input())
if no%5==0 and no%7==0:
   print("div by 5 and 7")
elif no%5==0:
   print("only 5")
elif no%7==0:
   print("only 7")
else:
   print("not div by 5 and 7")
