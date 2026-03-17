from abc import*
class shape(ABC):
	def __init__(self,name):
		self.name=name
	@abstractmethod
	def area(self):
		pass
class rectangle(shape):
	def __init__(self,n,L,B):
		super().__init__(n)
		self.L=L
		self.B=B
	def area(self):
		return self.L*self.B
class square(shape):
	def __init__(self,n,L):
		super().__init__(n)
		self.L=L
	def area(self):
		return self.L*self.L
r1=rectangle("rect",5,7)
print(r1.area())
s1=s++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++quare("sq",7)
print(s1.area())