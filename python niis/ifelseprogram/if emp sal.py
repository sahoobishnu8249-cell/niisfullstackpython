#WAP take emp salary from keyboard if sal>=5000 da=30% hra=20% then display basic salary da hra and total salary
print("enter basic salary")
sal=float(input())
da,hra=0,0
if sal>=5000:
   da=0.30*sal
   hra=0.20*sal
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)
