# import colorgram
#
# rgb_colors=[]
# colors=colorgram.extract('img.jpg',26)
#
# for i in colors:
#  r=i.rgb.r
#  g=i.rgb.g
#  b=i.rgb.b
#  new_colors=(r,g,b)
#  rgb_colors.append(new_colors)
#
# print(rgb_colors)


import turtle
import random
from turtle import Turtle
turtle.colormode(255)


rgb_colors=[(252, 251, 248), (244, 251, 249), (252, 248, 251), (242, 245, 249), (137, 81, 55), (184, 163, 125), (138, 167, 177), (63, 111, 133), (17, 41, 72), (137, 63, 88), (66, 118, 101), (160, 153, 47), (148, 181, 170), (214, 209, 112), (75, 34, 30), (71, 151, 162), (112, 40, 32), (95, 145, 120), (71, 30, 38), (176, 148, 162), (103, 42, 54), (166, 101, 128), (31, 55, 108), (107, 122, 164), (174, 107, 91), (207, 182, 194)]

tim=Turtle()

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(250)
tim.setheading(0)

for i in range(1,101):
    tim.dot(20, random.choice(rgb_colors))
    tim.forward(50)

    if i%10==0:
     tim.setheading(90)
     tim.forward(50)
     tim.setheading(180)
     tim.forward(500)
     tim.setheading(0)

screen=turtle.Screen()
screen.exitonclick()