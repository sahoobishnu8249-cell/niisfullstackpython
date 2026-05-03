class Node:
	def __init__(self,ele):
		self.data=ele
		self.next=None
f=Node(10)
s=Node(20)
t=Node(30)
f.next=s
s.next=t
t.next=None
ptr=f
while ptr!=None:
	print(ptr.data)
	ptr=ptr.next