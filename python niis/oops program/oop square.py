class square:
	def __init__(self,s):
		self.side=s
	def show(self):
		print("side=",self.side)
	def area(self):
		return self.side*self.side
	def perimeter(self):
		print("perimeter=",4*self.side)
s1=square(10)
s1.show()
print("area of square=",s1.area())
s1.perimeter()