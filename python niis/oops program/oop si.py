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
i1=simpleinterest(1000,10,2)
i1.show()
print("simple interest=",i1.sical())
