# Stack Program in Python using OOP
# Using top = -1 and MAX size variable

class Stack:
    MAX = 5

    def __init__(self):
        self.stack = [0] * self.MAX
        self.top = -1

    def push(self):
        if self.top == self.MAX - 1:
            print("Stack Overflow")
        else:
            item = int(input("Enter element to push: "))
            self.top = self.top + 1
            self.stack[self.top] = item
            print(item, "pushed into stack")

    def pop_element(self):
        if self.top == -1:
            print("Stack Underflow")
        else:
            item = self.stack[self.top]
            self.top = self.top - 1
            print(item, "popped from stack")

    def peek(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print("Top element is:", self.stack[self.top])

    def display(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            print("Stack elements are:")
            for i in range(self.top, -1, -1):
                print(self.stack[i])


# Object Creation
s = Stack()

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        s.push()

    elif choice == 2:
        s.pop_element()

    elif choice == 3:
        s.peek()

    elif choice == 4:
        s.display()

    elif choice == 5:
        print("Program Ended")
        break
    else:
        print("Invalid Choice")