class rectangle:
	def __init__(self,L,B):
		self.length=L
		self.breadth=B
	def show(self):
		print("length=",self.length)
		print("breadth=",self.breadth)
	def area(self):
		return self.length*self.breadth
	def perimeter(self):
		print("perimeter=",2*(self.length+self.breadth))
r1=rectangle(20,10)
r1.show()
print("area of rectangle=",r1.area())
r1.perimeter()