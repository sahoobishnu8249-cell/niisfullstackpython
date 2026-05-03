# Linked List Create and Display using OOP Concept
class Node:
    def __init__(self, ele):
        self.prev=None #new add
        self.data = ele
        self.next = None
class DLinkedList:
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
            if self.head == None:
                self.head = cur
            else:
                ptr.next = cur
                cur.prev=ptr #new add
            ptr = cur

            print("Do you continue? Press y/n")
            ch = input()

            if ch == "y":
                ch = True
            else:
                ch = False

    def displayf(self):
        if self.head==None:
            print("no element ")
            return 
        print("Elements are forward")
        ptr = self.head

        while ptr != None:
            print(ptr.data)
            ptr = ptr.next
    def displayb(self):
        if self.head==None:
            print("no element ")
            return
        print("elements in backward")
        ptr=self.head
        while ptr.next!=None:
            ptr=ptr.next
        while ptr!=None:
            print(ptr.data)
            ptr=ptr.prev
    def insertend(self,data):
        cur=Node(data)
        print("insert at the end id ",data)
        if self.head==None:
            self.head=cur
            return
        ptr=self.head
        while ptr.next !=None:
            ptr=ptr.next
        ptr.next=cur
        cur.prev=ptr


obj =DLinkedList()
obj.create()
obj.displayf()
obj.displayb()
obj.insertend(5)
obj.displayb()