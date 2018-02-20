#Robert Krall
#threelines.py


import turtle #import turtles library
wn = turtle.Screen()
wn.bgcolor("white")
alex = turtle.Turtle()
alex.color("black")
alex.pensize(3)
alex.speed(2)               #slowing down the turtle
alex.setposition(0,0)       #set position at middle


'''
#create every action one by one.
alex.left(90)               #putting angel north
alex.forward(200)           #going north of 200 steps
alex.penup()                #putting pen up
alex.right(90)
alex.forward(30)
alex.right(90)              #putting south
alex.pendown()
alex.forward(200)           #going south
alex.penup()                #putting tail up
alex.left(90)
alex.forward(30)
alex.left(90)
alex.pendown()
alex.forward(200)
'''

#Creating all three lines via a loop.
for i in range(4):
    if i % 2 == 0:  alex.left(90)
    else:           alex.right(90)
    alex.forward(200) #going north or south 200 steps
    alex.right(90)
    alex.penup()
    if i in [0,1]:      alex.forward(30) #invisible lat/long line for box 1
    elif i in [2,3]:    alex.forward(60) #invisible lat/long line for box 2
    if i == 1: alex.right(180) #route back to going north for box 2
    alex.pendown()

alex.penup()
alex.setposition(0,0)
wn.exitonclick()        #only exit on click
