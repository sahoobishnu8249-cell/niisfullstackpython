# Circular Queue Program in Python (Without OOP)

MAX = 5
queue = [0] * MAX
front = -1
rear = -1


def enqueue():
    global front, rear

    # Check Overflow
    if (front == 0 and rear == MAX - 1) or (rear == front - 1):
        print("CQ Overflow")

    else:
        item = int(input("Enter element to insert: "))

        if front == -1:
            front = 0

        if rear == MAX - 1:
            rear = 0
        else:
            rear = rear + 1

        queue[rear] = item
        print(item, "insert into CQueue")


def dequeue():
    global front, rear

    # Check Underflow
    if front == -1:
        print("CQ Underflow")

    else:
        item = queue[front]
        print(item, "delete from CQueue")

        if front == rear:
            front = -1
            rear = -1
            return

        if front == MAX - 1:
            front = 0
            return

        front = front + 1


def peek():
    if front == -1:
        print("CQ is Empty")
    else:
        print("Front element is:", queue[front])


def display():
    if front == -1:
        print("CQ is Empty")

    else:
        print("CQ elements are:")

        if front <= rear:
            for i in range(front, rear + 1):
                print(queue[i])

        else:
            for i in range(front, MAX):
                print(queue[i])

            for i in range(0, rear + 1):
                print(queue[i])


# Main Menu
while True:
    print("\n--- CIRCULAR QUEUE MENU ---")
    print("1. Insert")
    print("2. Delete")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        enqueue()

    elif choice == 2:
        dequeue()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")