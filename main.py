# ---------------------- Ignore this unless you wish to generate other colors -------------- #
# import colorgram

# --------- This is to generate the rgb colors from an image - Extracted colors below --------- #
# colors_1 = colorgram.extract('image1.jpg', 30)
# color_list = []
#
# for i in range(0, 30):
#     color_tuple = ()
#     first_color = colors_1[i]
#     rgb = first_color.rgb
#     color_tuple += rgb
#     color_list.append(color_tuple)
#
# print(color_list)


import turtle
import random

turtle.colormode(255)
dots = turtle.Turtle()

# Deleted some of the white colors and kept gray and off whites
colors = [(246, 239, 242), (240, 246, 243), (132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
counter = 0
dots.hideturtle()
dots.penup()
dots.goto(-250, -200)

while counter < 100:
    dots.pendown()
    dots.dot(20, random.choice(colors))
    dots.penup()
    dots.forward(50)
    counter += 1
    # Move pen to next row
    if counter % 10 == 0:
        dots.left(90)
        dots.forward(50)
        dots.left(90)
        dots.forward(500)
        dots.left(180)


screen = turtle.Screen()
screen.exitonclick()
