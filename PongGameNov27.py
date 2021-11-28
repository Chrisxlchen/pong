# Import required library
import turtle
import os

# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
sc.tracer(0)

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)  #
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Ball of circle shape
hit_ball = turtle.Turtle()
hit_ball.speed(40)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 0.1
hit_ball.dy = -0.1


# Functions to move paddle vertically
def left_paddle_up():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)


def left_paddle_down():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)


def right_paddle_up():
    y = right_pad.ycor()
    y += 20
    right_pad.sety(y)


def right_paddle_down():
    y = right_pad.ycor()
    y -= 20
    right_pad.sety(y)


# Keyboard bindings
sc.listen()
sc.onkeypress(left_paddle_up, "e")
sc.onkeypress(left_paddle_down, "d")
sc.onkeypress(right_paddle_up, "Up")
sc.onkeypress(right_paddle_down, "Down")

while True:
    sc.update()

    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Checking borders
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1
        os.system("afplay bounce.wav&")

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1
        os.system("afplay bounce.wav&")

    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1

    # Paddle ball collision
    if (370 > hit_ball.xcor() > 360) and (
            right_pad.ycor() + 40 > hit_ball.ycor() > right_pad.ycor() - 40):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (-360 > hit_ball.xcor() > -370) and (
            left_pad.ycor() + 40 > hit_ball.ycor() > left_pad.ycor() - 40):
        hit_ball.setx(-360)
        hit_ball.dx *= -1

