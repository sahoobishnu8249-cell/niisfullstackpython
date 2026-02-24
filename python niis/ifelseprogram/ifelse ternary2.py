#WAP take emp salary from keyboard if sal>=5000 da=30% hra=20% if sal<5000 da=20% hra=10% then display basic salary da hra and total salary 
print("enter basic salary")
sal=float(input())
da=0.30*sal if sal>=5000 else 0.2*sal
hra=0.20*sal if sal>=5000 else 0.1*sal
totalsal=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",totalsal)
