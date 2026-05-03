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
        ch =1
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

            print("Do you continue? Press 1")
            ch = int(input())

    def display(self):
        print("elements are")
        ptr=self.head
        while ptr.next!=self.head:
            print(ptr.data)
            ptr=ptr.next
        print(ptr.data)
    def insertbeg(self):
        cur=Node(5)
        if self.head==None:
            cur.next=cur
            self.head=cur
            return
        ptr=self.head
        while ptr.next!=self.head:
            ptr=ptr.next
        ptr.next=cur
        cur.next=self.head
        self.head=cur

obj =CLinkedList()
obj.create()
obj.display()
obj.insertbeg()
obj.display()
