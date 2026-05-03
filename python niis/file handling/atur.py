import pickle
class student:
	def __init__(self,roll,name,mark):
		self.roll=roll
		self.name=name
		self.mark=mark
	def show(self):
		print(self.roll,self.name,self.mark)
f=open("student.dat","rb")
print("student records:")
while True:
	try:
		s=pickle.load(f)
		s.show()
	except EOFError:
		break
f.close()