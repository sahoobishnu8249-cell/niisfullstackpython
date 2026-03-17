class student:
	def __init__(self,name):
		self.__name=name
	@property
	def name(self):
		return self.__name
	@name.setter
	def name(self,value):
		self.__name=value
s=student("Muna")
print(s.name)
s.name="Rahul"
print(s.name)
	
