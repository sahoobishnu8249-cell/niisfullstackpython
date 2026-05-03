from tkinter import *
def add():
	n1=int(e1.get())
	n2=int(e2.get())
	n3=int(e3.get())
	result=n1+n2+n3
	lbl.config(text="result = " + str(result))

root = Tk()
root.title("Addition App")
root.geometry("300x200")
Label(root, text="Enter first number").pack()
e1 = Entry(root)
e1.pack()
Label(root, text="Enter second number").pack()
e2 = Entry(root)
e2.pack()
Label(root, text="Enter third number").pack()
e3 = Entry(root)
e3.pack()
Button(root, text="Add", command=add).pack()
lbl = Label(root, text="")
lbl.pack()
root.mainloop()