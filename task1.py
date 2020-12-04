import turtle

"""
this text is not read by the computer
because it is enclosed by tripple double quotes (3 ") 

Here are some building blocks for using turtle

forward(n) move forward n pixels
backward(n) move backward n pixels
right(a) turn right a degrees
left(a) turn left a degrees

penup() lifts the pen so that the turtle is no longer dwaring
pendown() lowers the pen so that the turtle is once again drawing

goto(x,y) go to position x,y
setheading(a) sets the way the turtle is facing where east is 0, north is 90, west is 180, etc


Use these building blocks to draw a house with 1 door and 2 windows

also, lines that start with a # are ignored by the computer
such lines are called comments
this block inside the tripple " is a block comment

comments are VERY HEALTHY it helps people read your code
"""

#here is a bit to get you started
smith = turtle.Turtle()

#set the speed of smith
smith.speed(1)

#tell smith to go forward 100
smith.forward(100)

#tell smith to pick up his pen
smith.penup()

#tell smith to turn right 120 degrees
smith.right(120)

#tell smith to go forward 100
smith.forward(100)

#tell smith to put his pen down so he starts drawing
smith.pendown()

#tell smith to turn right 60 degrees
smith.right(60)

#tell smith to go backwards 100
smith.backward(100)


turtle.exitonclick()
