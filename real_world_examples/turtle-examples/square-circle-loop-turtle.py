import turtle

def draw_square(some_turtle_name):
    for i in range(1,5):
        some_turtle_name.forward(100)
        some_turtle_name.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(10)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    window.exitonclick()

draw_art()


