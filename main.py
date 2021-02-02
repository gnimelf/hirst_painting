# import colorgram

# Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 25)
#
# random_color_list = []
# for color in colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     new_color = (r, g, b)
#     random_color_list.append(new_color)

# print(random_color_list)

from turtle import Turtle, Screen
import random
tim = Turtle()
tim.hideturtle()
tim.penup()
x = -325
y = -325
tim.goto(x, y)
screen = Screen()
screen.colormode(255)

color_list = [(230, 215, 101), (234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18),
              (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23),
              (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25),
              (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163)]

for line in range(10):
    for dot in range(10):
        dot_color = random.choice(color_list)
        # print(dot_color)
        tim.dot(20, dot_color)
        tim.forward(50)
    y += 50
    tim.goto(x, y)

screen.exitonclick()