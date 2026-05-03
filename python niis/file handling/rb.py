import pickle
f=open("xyz.dat","rb")
L=pickle.load(f)
print(L)
f.close()