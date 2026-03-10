class student:
	def __init__(self,n,r,m):
		self.__name=n
		self.__roll=r
		self.__mark=m
	def show(self):
		print("my name=",self.__name)
		print("my rollno=",self.__roll)
		print("my mark=",self.__mark)
	def update(self,n,r,m):
		self.__name=n
		self.__roll=r
		self.__mark=m
	def set__Name(self,name):
		self.__name=name
	def set__Roll(self,roll):
		self.__roll=roll
	def set__Mark(self,mark):
		self.__roll=roll
	def get__Name(self,name):
		self.__name=name
	def get__Roll(self,roll):
		self.__roll=roll
	def get__Mark(self,mark):
		self.__roll=roll
s=student("muna",1,90.78)
s.show()
s.update("muna das",2,90.87)
s.show()
