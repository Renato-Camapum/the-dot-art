# import colorgram
# rgb_colors = []
# colors = colorgram.extract('dots.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)

color_list = [(240, 240, 239), (230, 232, 237), (232, 238, 235), (239, 233, 236), (187, 161, 122), (14, 25, 57), (67, 94, 134), (145, 87, 55), (139, 158, 184), (139, 73, 94), (68, 15, 6), (186, 141, 160), (24, 51, 126), (71, 110, 85), (129, 29, 51), (149, 21, 8), (183, 148, 46), (138, 169, 151), (215, 206, 136), (62, 18, 30), (93, 118, 178), (187, 93, 115), (187, 97, 82), (14, 34, 29), (97, 146, 129), (222, 174, 188), (33, 84, 64), (162, 208, 183), (180, 186, 211), (91, 145, 154)]
tim = Turtle()
tim.hideturtle()
tim.penup()
pos_x = -300
pos_y = -220
tim.goto(pos_x, pos_y)


for _ in range(10):
    for _ in range(10):
        color_rgb = random.choice(color_list)
        tim.pencolor(color_rgb)
        tim.fd(50)
        tim.dot(20)

    pos_y += 50
    tim.goto(pos_x, pos_y)


screen.exitonclick()
