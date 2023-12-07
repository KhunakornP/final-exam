import turtle
import random


class Polygon:
    def __init__(self, sides):
        self.sides = sides
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300),
                         random.randint(-200, 200)]
        self.color = self.get_new_color()
        self.border_size = random.randint(1, 10)

    def get_new_color(self):
        return (random.randint(0, 255),
                random.randint(0, 255), random.randint(0, 255))

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.sides):
            turtle.forward(self.size)
            turtle.left(360/self.sides)
        turtle.penup()

    def reduce_ratio(self):
        reduction_ratio = 0.618
        self.size *= reduction_ratio
        turtle.penup()
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.left(90)
        turtle.forward(self.size * (1 - reduction_ratio) / 2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]


# main part
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)
rand_poly = 20
number = input("Which art do you want to generate? \n"
               "Enter a number between 1 to 8,inclusive:")
if not number.isdigit():
    print("Invalid number.")
else:
    if int(number) == 1:
        for i in range(rand_poly):
            x = Polygon(3)
            x.draw_polygon()
    elif int(number) == 2:
        for i in range(rand_poly):
            x = Polygon(4)
            x.draw_polygon()
    elif int(number) == 3:
        for i in range(rand_poly):
            x = Polygon(5)
            x.draw_polygon()
    elif int(number) == 4:
        for i in range(rand_poly):
            sides = random.randint(3,5)
            x = Polygon(sides)
            x.draw_polygon()
    elif int(number) == 5:
        for i in range(rand_poly):
            x = Polygon(3)
            x.draw_polygon()
            x.reduce_ratio()
            x.draw_polygon()
            x.reduce_ratio()
            x.draw_polygon()
    elif int(number) == 6:
        for i in range(rand_poly):
            x = Polygon(4)
            x.draw_polygon()
            x.reduce_ratio()
            x.draw_polygon()
            x.reduce_ratio()
            x.draw_polygon()
    elif int(number) == 7:
        for i in range(rand_poly):
            x = Polygon(5)
            x.draw_polygon()
            x.reduce_ratio()
            x.draw_polygon()
            x.reduce_ratio()
            x.draw_polygon()
    elif int(number) == 8:
        for i in range(rand_poly):
            sides = random.randint(3, 5)
            x = Polygon(sides)
            x.draw_polygon()
            x.reduce_ratio()
            x.draw_polygon()
            x.reduce_ratio()
            x.draw_polygon()
    else:
        print("Number not in range.")

turtle.done()