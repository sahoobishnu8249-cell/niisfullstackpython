#WAP take a string
print("enter a string")
s=input()
c,alp,up,lw,vw,co,dg,sp,sy,wd=0,0,0,0,0,0,0,0,0,0
for i in s:
	c=c+1
	if i.isalpha():
		alp=alp+1
		if i.isupper():
			up=up+1
		else:
			lw=lw+1
		if i in "aeiouAEIOU":
			vw=vw+1
		else:
			co=co+1
	elif i.isdigit():
		dg=dg+1
	elif i.isspace():
		sp=sp+1
	else:
		sy=sy+1
wd=sp+1
print("no of char=",c)
print("no of alpha=",alp)
print("no of up=",up)
print("no of lw=",lw)
print("no of vw=",vw)
print("no of co=",co)
print("no of digit=",dg)
print("no of space=",sp)
print("no of sy=",sy)
print("no of word=",wd)