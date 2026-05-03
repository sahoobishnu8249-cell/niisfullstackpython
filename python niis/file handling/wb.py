import pickle
numbers=[10,20,30,40,50]
f=open("xyz.dat","wb")
pickle.dump(numbers,f)
f.close()