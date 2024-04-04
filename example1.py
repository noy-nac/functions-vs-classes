
from turtle import Turtle, Screen

screen = Screen()
screen.register_shape("paddle.gif")

leftX = -100
rightX = 100

left  = Turtle()
right = Turtle()

def leftUp():
    left.setheading(90)
    left.forward(10)

def leftDown():
    left.setheading(270)
    left.forward(10)

def rightUp():
    right.setheading(90)
    right.forward(10)

def rightDown():
    right.setheading(270)
    right.forward(10)

left.penup()
right.penup()

left.shape("paddle.gif")
right.shape("paddle.gif")

left.goto(leftX, 0)
right.goto(rightX, 0)

screen.onkeypress(leftUp, 'w')
screen.onkeypress(leftDown, 's')
screen.onkeypress(rightUp, 'Up')
screen.onkeypress(rightDown, 'Down')
screen.listen()

screen.mainloop()