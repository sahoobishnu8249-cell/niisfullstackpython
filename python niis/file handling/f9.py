f=open("data.txt","r")
f.seek(10)
print(f.read())
print(f.tell())