#WAP take no from keyboard check no is sd dd and od using elif
print("enter a number")
no=int(input())
if no<0:
   no=-no
#check
if no<10:
   print("sd")
elif no<100:
   print("dd")
elif no<1000:
   print("td")
else:
   print("od")