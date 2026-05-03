# double circular Linked List Create and Display using OOP Concept
class Node:
    def __init__(self, ele):
        self.prev=None
        self.data = ele
        self.next = None
class DCLinkedList:
    def __init__(self):
        self.head = None
    def create(self):
        ch =1
        c = 0
        ptr = None
        while ch==1:
            c = c + 1
            print("Enter node", c, "data")
            ele = int(input())
            cur = Node(ele)
            cur.prev=cur
            cur.next=cur
            if self.head == None:
                self.head = cur
            else:
                ptr.next = cur
                cur.next=self.head
                cur.prev=ptr
                self.head.prev=cur
            ptr = cur
            print("Do you continue? Press 1")
            ch = int(input())
    def displayf(self):
        if self.head==None:
            print("no element ")
            return
        print("Elements are forward")
        ptr =self.head
        while ptr.next != self.head:
            print(ptr.data)
            ptr = ptr.next
        print(ptr.data)
    def displayb(self):
        if self.head==None:
            print("no element ")
            return
        print("Elements are backward")
        ptr=self.head.prev
        while ptr.prev!=self.head.prev:
            print(ptr.data)
            ptr=ptr.prev
        print(ptr.data)
      
    def deletebeg(self):
        if self.head==None:
            print("List is empty")
            return
        if self.head.next == self.head:
            print("delete element=",self.head.data)
            self.head = None
            return
        print("delete element=",self.head.data)      
        self.head.next.prev = self.head.prev  
        self.head = self.head.next       
        self.head.prev.next = self.head       
obj =DCLinkedList()
obj.create()
obj.displayf()
obj.displayb()
obj.deletebeg()
obj.displayf()
obj.displayb()









