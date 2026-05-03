import threading
class Test:
	def disp(self):
		for i in range(5):
			print("hello")
	def show(self):
		for i in range(5):
			print("bye")
ob=Test()
t1=threading.Thread(target=ob.disp)
t2=threading.Thread(target=ob.show)
t1.start()
t2.start()
