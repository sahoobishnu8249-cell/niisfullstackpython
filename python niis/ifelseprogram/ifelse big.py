#WAP take 3 number from keyboard display biggest number
print("enter three nos")
no1=int(input())
no2=int(input())
no3=int(input())
if no1>=no2:
   if no1>=no3:
      print("first number is bigger",no1)
   else:
      print("third number is bigger",no3)
else:
   if no2>=no3:
      print("second number is bigger",no2)
   else:
      print("third number is bigger",no3)