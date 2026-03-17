from abc import*
class Animal(ABC):
	@abstractmethod
	def sound(self):
		pass
class Dog(Animal):
	def sound(self):
		return "Bark"
d=Dog()
print(d.sound())

