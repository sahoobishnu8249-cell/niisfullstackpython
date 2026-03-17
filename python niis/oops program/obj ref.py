class Demo():
	def __init__(self,n):
		self.n=n
		print("constructor",self.n)
	def __del__(self):
		print("destructor",self.n)
d1=Demo("first")
d2=d1
d3=d2
print("hi")