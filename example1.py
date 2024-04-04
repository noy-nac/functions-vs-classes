
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

left.penup()

left.shape("paddle.gif")

left.goto(leftX, 0)

screen.onkeypress(leftUp, 'w')
screen.onkeypress(leftDown, 's')
screen.listen()

screen.mainloop()