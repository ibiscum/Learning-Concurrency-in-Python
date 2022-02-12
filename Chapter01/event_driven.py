""" Learning Concurrency in Python - Chapter 01 - event driven """

import turtle

turtle.setup(500, 500)
window = turtle.Screen()
window.title("Event Handling 101!")
window.bgcolor("lightblue")
nathan = turtle.Turtle()


def move_forward():
    nathan.forward(50)


def move_left():
    nathan.left(30)


def move_right():
    nathan.right(30)


def start():
    window.onkey(move_forward, "Up")
    window.onkey(move_left, "Left")
    window.onkey(move_right, "Right")
    window.listen()
    window.mainloop()


if __name__ == '__main__':
    start()
