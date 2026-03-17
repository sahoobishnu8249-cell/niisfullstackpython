class Mytime:
	def __init__(self,h,m,s):
		self.h=h
		self.m=m
		self.s=s
	def __str__(self):
		return str(self.h)+":"+str(self.m)+":"+str(self.s)
t1=Mytime(5,40,35)
print(t1)
print(t1.__str__())