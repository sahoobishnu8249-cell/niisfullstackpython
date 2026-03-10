a=10
def show():
	a=30
	print(a)
	print(locals()['a'])
	print(globals()['a'])
	globals()['a']=40
show()
print(a)