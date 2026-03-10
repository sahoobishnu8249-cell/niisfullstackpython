class simpleinterest:
	def __init__(self,p,t,r):
		self.principal=p
		self.time=t
		self.rate=r
	def show(self):
		print("principal=",self.principal)
		print("time=",self.time)
		print("rate=",self.rate)
	def sical(self):
		return self.principal*self.time*self.rate/100
print("enter principal time and rate")
#i1=		
