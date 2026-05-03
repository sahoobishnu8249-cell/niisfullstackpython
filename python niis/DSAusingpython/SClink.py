# Linked List Create and Display using OOP Concept
class Node:
    def __init__(self, ele):
        self.prev=None #new add
        self.data = ele
        self.next = None
class CLinkedList:
    def __init__(self):
        self.head = None
    def create(self):
        ch = True
        c = 0
        ptr = None
        while ch:
            c = c + 1
            print("Enter node", c, "data")
            ele = int(input())
            cur = Node(ele)
            cur.next=cur
            if self.head == None:
                self.head = cur
            else:
                ptr.next = cur
                
                cur.next=self.head #new add
            ptr = cur

            print("Do you continue? Press y/n")
            ch = input()

            if ch == "y":
                ch = True
            else:
                ch = False

    def display(self):
        print("elements are")
        ptr=self.head
        while ptr.next!=self.head:
            print(ptr.data)
            ptr=ptr.next
        print(ptr.data)
obj =CLinkedList()
obj.create()
obj.display()
