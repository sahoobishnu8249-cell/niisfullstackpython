MAX=5
stack=[0]*MAX
top=-1
def push():
	global top
	if top==MAX-1:
		print("Stack Overflow")
	else:
		item=int(input("Enter element to push:"))
		top=top+1
		stack[top]=item
		print(item,"pushed into stack")
def pop_element():
	global top

	if top==-1:
		print("Stack Underflow")
	else:
		item=stack[top]
		top=top-1
		print(item,"poped from stack")
def peek():
	if top==-1:
		print("Stack is empty")
	else:
		print("Top element is:", stack[top])
def display():
	if top==-1:
		print("Stack is empty")
	else:
		print("Stack elements are:")
		for i in range(top,-1,-1):
			print(stack[i])
while True:
	print("\n--- STACK MENU ---")
	print("1. Push")
	print("2. Pop")
	print("3. Peek")
	print("4. Display")
	print("5. Exit")
	choice=int(input("Enter your choice:"))
	if choice==1:
		push()
	elif choice==2:
		pop_element()
	elif choice==3:
		peek()
	elif choice==4:
		display()
	elif choice==5:
		print("Program ended")
		break
	else:
		print("Invalid Choice")















