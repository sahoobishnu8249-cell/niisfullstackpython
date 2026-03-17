#parent class
class person:
	def __init__(self,name,age):
		self.name=name
		self.age=age
	def show_person(self):
		print("Name:",self.name)
		print("Age:",self.age)

#child class
class student(person):
	def __init__(self,name,age,roll):
		super().__init__(name,age)
		self.roll=roll
	def show_student(self):
		print("Rollno:",self.roll)

#grant child class
class Enggstudent(student):
	def __init__(self,name,age,roll,branch):
		super().__init__(name,age,roll)
		self.branch=branch
	def show_engg(self):
		print("Branch:",self.branch)
#object creation
e=Enggstudent("Bishnu",20,101,"cs")
e.show_person()
e.show_student()
e.show_engg()
