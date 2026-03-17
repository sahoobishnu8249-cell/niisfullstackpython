class Demo:
	def __init__(self):
		print("constructor")
	def __del__(self):
		print("destructor")

Demo()
print("hi")