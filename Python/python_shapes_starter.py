'''
Some turtle functions you can use to make your shapes


forward(<distance>) - This function takes a positive or negative number and
will move the turtle forward.

back(<distance>) - This function takes a positive or negative numbers and
it will move the turtle back.

right(<angle>) - This function takes a number that represents
angle in degrees. It will turn the turtle to  its right

left(<angle>) - This functions takes an number that represents
 an angle in degrees. It will turn the turtle to its left.

pencolor(<color>) - This functions takes a string that represents a color. The
turtle's pen will draw in that color. The possible color values can be found
at https://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm

penup() - This function takes no parameters. When called it will
lift the turtle's pen up, the turtle will not draw when moved.

pendown() - This function takes no parameters. When called it will put the
turtle's pen down. It will draw when moved.

speed(<number>) - This function takes a number. It determines how fast the
turtle moves around the screen. Strangely enough if you want it to go as
fast as possible you have to pass it 0 as a parameter.

goto(<x>, <y>) - This function takes two numbers, a position along the x-axis
and a position along the y-axis. It will move the turtle to that position.

fillcolor(<color>) - This function takes a string that represents a color. The
color will be used to fill shape the turtle has made. In order to get the turtle
to fill the shape you have to use the begin_fill() function before the turtle
starts drawing the shape and the end_fill() function after it finishes for the
shape to be filled in.

begin_fill() - This function takes no parameters. It is put before the turtle
draws a shape that you want filled in.

end_fill() - This function takes no parameters. It is put after the turtle has
finished drawing a shape that you want filled in.

dot(<size>, <color>) - This function takes two parameters. The first is a
positive number that represents the diameter of the dot to be drawn by the
turtle. The second is a string that represents the color the dot should be.


BONUS:

circle(<radius>, <extent>, <steps>) - This function takes three parameters.
However you only have to put in the first one. The <radius> parameter is the
necessary parameter, it is a number that represents the radius of the circle.
The <extent> is optional. It represents an angle saying how much of the circle
should be drawn, if you don't put in anything for <extent> it will draw the whole
circle. If you put in 180, it will draw a half circle. The third parameter
<steps> is a number that represents how many steps the turtle should take to
draw the circle. Try setting <steps> as 5 to see what happens.


'''




from turtle import *
import turtle

# length = 80
# def square (side_length, colour):
# 	for i in range (4):
# 		pencolor(colour)
# 		forward (side_length)
# 		right (90)

# pendown()
# square (50, "tomato")
# penup()
# forward (length)
# pendown()
# square (80, "DarkOrchid")
# penup()
# forward (length+length)
# pendown()
# square (110, "turquoise")
# penup()
# forward (length+length+length)
# turtle.done()

# length = 80
# def triangle (side_length, colour):
# 	for i in range (3):
# 		pencolor(colour)
# 		forward (side_length)
# 		right (-120)

# pendown()
# triangle(50, "thistle")
# penup()
# forward(length)
# pendown()
# triangle(80, "salmon")
# penup()
# forward(length+length)
# pendown()
# triangle(110, "PaleGreen")
# penup()
# forward(length+length+length)
# turtle.done()

# length = 110
# def hexagon (side_length, colour):
# 	for i in range (6):
# 		pencolor(colour)
# 		forward (side_length)
# 		right (60)

# pendown()
# hexagon(50, "NavyBlue")
# penup()
# forward(length)
# pendown()
# hexagon(80, "maroon1")
# penup()
# forward(length+length)
# pendown()
# hexagon(110, "MediumAquamarine")
# penup()
# forward(length+length+length)
# turtle.done()

# length = 210
# penup()
# goto (-310,0)
# def octogon (side_length, colour):
# 	for i in range (8):
# 		pencolor(colour)
# 		forward (side_length)
# 		right (45)

# pendown()
# octogon(50, "medium slate blue")
# penup()
# forward(length)
# pendown()
# octogon(80, "magenta")
# penup()
# forward(length+10)
# pendown()
# octogon(110, "goldenrod")
# penup()
# forward(length)
# turtle.done()

user_choice = int(input("How many sides do you want?"))
colour = input("What colour do you want?")
size = int(input("What size do you want it?"))

def polygon (sides):
	pencolor(colour) 
	sides = user_choice
	for i in range (user_choice):
		pendown()
		forward(size)
		right(360/sides)
polygon(user_choice)
turtle.done()