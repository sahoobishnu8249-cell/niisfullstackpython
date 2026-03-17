class Demo:
	def __init__(self):
		print("constructor")
	def __del__(self):
		print("destructor")
d1=Demo()
d2=Demo()
d3=Demo()
print("hi")