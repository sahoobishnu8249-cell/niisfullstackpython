class student:
	def __init__(self,n,r,m):
		self.name=n
		self.roll=r
		self.mark=m
	def show(self):
		print("my name=",self.name)
		print("my rollno=",self.roll)
		print("my mark=",self.mark)
s1=student("muna",1,90.30)
s2=student("kuna",2,80.30)
s1.show()
s2.show()