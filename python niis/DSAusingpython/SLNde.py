# Linked List Create and Display using OOP Concept

class Node:
    def __init__(self, ele):
        self.data = ele
        self.next = None


class LinkedList:
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

            ptr = cur

            print("Do you continue? Press True/False")
            ch = input()

            if ch == "True":
                ch = True
            else:
                ch = False

    def display(self):
        print("Elements are")
        ptr = self.head

        while ptr != None:
            print(ptr.data)
            ptr = ptr.next
    
        
    def deleteend(self):
        if self.head==None:
            print("List is empty")
            return
        if self.head.next==None:
            print("Deleted element:", self.head.data)
            self.head = None
            return
        ptr = self.head
        while ptr.next.next!=None:
            ptr = ptr.next
        print("Deleted element:", ptr.next.data)
        ptr.next = None
            

        
obj = LinkedList()
obj.create()
obj.display()

obj.deleteend()
obj.display()