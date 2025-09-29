from turtle import *


# we want to paint a house

# step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

# step 2: draw a door
 
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

# step 3: draw a roof

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

# step 4: draw a windows

penup()
goto(150, 100)
pendown()

color("brown")
begin_fill()
right(150)
forward(50)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)

penup()
goto(50, 100)
pendown()

forward(30)
right(90)
forward(50)
right(90)
forward(30)
right(90)
forward(50)
end_fill()

exitonclick()