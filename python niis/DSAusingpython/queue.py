MAX=5
queue=[0]*MAX
front,rear=-1,-1
def enqueue():
	global rear,front
	if rear==MAX-1:
		print("Queue Overflow")
	else:
		item=int(input("Enter element to push:"))
		if front==-1:
			front=0
		rear=rear+1
		queue[rear]=item
		print(item,"insert into queue")
def dequeue():
	global rear,front

	if front==-1:
		print("Queue Underflow")
	else:
		item=queue[front]
		front=front+1
		print(item,"delete from queue")
def peek():
	if front==-1:
		print("queue is empty")
	else:
		print("Top element is:", queue[front])
def display():
	if front==-1:
		print("Queue is empty")
	else:
		print("Queue elements are:")
		for i in range(front,rear+1,1):
			print(queue[i])
while True:
	print("\n--- QUEUE MENU ---")
	print("1. insert")
	print("2. delete")
	print("3. Peek")
	print("4. Display")
	print("5. Exit")
	choice=int(input("Enter your choice:"))
	if choice==1:
		enqueue()
	elif choice==2:
		dequeue()
	elif choice==3:
		peek()
	elif choice==4:
		display()
	elif choice==5:
		print("Program ended")
		break
	else:
		print("Invalid Choice")















