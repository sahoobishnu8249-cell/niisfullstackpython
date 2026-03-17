import turtle
import random

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Happy Birthday Situ")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Function to draw stars
def draw_star(x, y, color):
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.color(color)
    star.penup()
    star.goto(x, y)
    star.pendown()
    
    for i in range(5):
        star.forward(20)
        star.right(144)

# Draw random stars
colors = ["red", "yellow", "blue", "green", "pink", "orange"]
for i in range(30):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    draw_star(x, y, random.choice(colors))

# Write Happy Birthday
pen.color("white")
pen.penup()
pen.goto(0, 0)
pen.write("Happy Birthday Situ!", align="center", font=("Arial", 40, "bold"))

# Write message
pen.goto(0, -60)
pen.write("Have a Wonderful Day!", align="center", font=("Arial", 20, "normal"))

turtle.done()