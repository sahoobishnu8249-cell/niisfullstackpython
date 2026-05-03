f = open("data.txt", "r")
L=f.readlines()
for i in L:
	print(i,end="")
f.close()