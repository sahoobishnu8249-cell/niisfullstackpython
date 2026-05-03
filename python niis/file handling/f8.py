#copy one file another file
f1=open("data.txt", "r")
f2=open("data2.txt","w")
f2.write(f1.read())
f1.close()
f2.close()