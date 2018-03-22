import turtle


my_turtle = turtle.Turtle()
my_turtle.showturtle()
my_screen = turtle.Screen()
my_screen.bgcolor("Pink")
my_turtle.shape("turtle")
my_turtle.speed(0)


my_turtle.width(2)
my_turtle.fillcolor("Purple")
my_turtle.begin_fill() # starting a new object that we will fill in
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill()


my_turtle.begin_fill()
my_turtle.up() # picking the pencil up
my_turtle.goto(200, 200)
my_turtle.down() # puts pencil down
my_turtle.goto(250, 250)
my_turtle.goto(250, 200)
my_turtle.goto(200, 200)
my_turtle.fillcolor("Black")
my_turtle.end_fill()


my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()

# move with headings
my_turtle.begin_fill()
my_turtle.forward(100)
my_turtle.setheading(90)
my_turtle.forward(100)
my_turtle.setheading(180)
my_turtle.forward(100)
my_turtle.setheading(270)
my_turtle.forward(100)
my_turtle.end_fill()


# Recursive rectangle pattern


my_screen.clear() # clears out the screen


def recursive_rect(width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(width, height)
        my_turtle.down()
        my_turtle.goto(width, -height)
        my_turtle.goto(-width, -height)
        my_turtle.goto(-width, height)
        my_turtle.goto(width, height)
        recursive_rect(width * 1.5, height * 1.5, depth - 1)

recursive_rect(3, 5, 5)

my_screen.clear()


def recursive_ncaa(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.goto(x + size, y)
        my_turtle.goto(x + size, y + size / 2)
        my_turtle.goto(x + size, y - size / 2)
        recursive_ncaa(x + size, y + size / 2, size / 2, depth - 1)
        recursive_ncaa(x + size, y - size / 2, size / 2, depth - 1)

recursive_ncaa(-300, 0, 300, 5)
my_screen.exitonclick()


# my_turtle.hidturtle() -- the oposit of show turtle
# my_turtle.xcor() and .ycor() -- x, y positions