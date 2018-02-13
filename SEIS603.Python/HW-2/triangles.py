#Robert Krall
#mileage.py


import turtle #import turtles library
wn = turtle.Screen()
wn.bgcolor("white")
alex = turtle.Turtle()
alex.color("black")
alex.pensize(3)
alex.speed(2)               #slowing down the turtle
alex.setposition(0,0)       #set position at middle

#making both triangles
for i in range(9):
    if i == 0: alex.left(60) #makes angle for left corner for big triangle
    elif i == 7: alex.right(60) #draws the line straight in the middle
    else: alex.right(120)
    if i == 0 or i == 1 or i == 2: alex.forward(200) #lines for outside triangle
    else: alex.forward(100) #lines for inside triangle

alex.penup()
alex.setposition(0,0)
wn.exitonclick()        #only exit on click
