#WAP to calculate electricity bill
units=int(input("enter total electricity units consumed:"))
bill=0
if units<=100:
	bill=units*1.5
elif units<=200:
	bill=(100*1.5)+(units-100)*2.5
elif units<=300:
	bill=(100*1.5)+(100*2.5)+(units-200)*4.0
else:
	bill=(100*1.5)+(100*2.5)+(100*4.0)+(units-200)*6.0
print("total bill=",round(bill,2))

