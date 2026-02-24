#WAP to calculate area of square,rectangle,and circle
import math
print("choose a shape to calculate area:")
print("1.square")
print("2.rectangle")
print("3.circle")
choice=int(input("enter your choice(1-3):"))
if choice==1:
   side=float(input("enter the side of the square:"))
   area=side*side
   print("area of square=",area)
elif choice==2:
   length=float(input("enter the length of the rectangle:"))
   breadth=float(input("enter the breadth of the rectangle:"))
   area=length*breadth
   print("area of rectangle=",area)
elif choice==3:
   radius=float(input("enter the radius of the circle:"))
   area=math.pi*radius*radius
   print("area of circle=",area)
else:
   print("invalid choice")