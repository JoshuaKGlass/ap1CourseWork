# pythagoras script
# screen = creates area for turtle.
# Turtle = import turtle lib.
# mainloop = for interactive use of turtle graphics.
from turtle import Screen, Turtle, mainloop


class PythagorasTurtle(Turtle):
    def __init__(self, x, y):
        Turtle.__init__(self)
        self.shape("turtle")
        self.resizemode("user")
        self.shapesize(3, 3, 5)
        self.pensize(10)
        self.forward(100)  # set base

        self.left(135)  # change direction
        self.forward(142)  # set angle forward

        self.left(135)  # change direction
        self.forward(100)  # go forward

        self.ondrag(self.shift)

    def shift(self, x, y):
        self.sety(max(0, min(y, 1)))


def createTriangle():
    writer = Turtle()
    writer.forward(100)  # set base

    writer.left(135)  # change direction
    writer.forward(142)  # set angle forward

    writer.left(135)  # change direction
    writer.forward(100)  # go forward


def main():
    # need to create triangle and able
    # to set pos x and pos y coordinates
    global screen, red, green, blue
    screen = Screen()
    screen.delay(0)
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)
    createTriangle()

    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.goto(1, 1.15)
    return "EVENTLOOP"


if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
