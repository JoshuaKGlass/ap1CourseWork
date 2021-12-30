from turtle import Screen, Turtle, mainloop

class trigY(Turtle):
    def __init__(self, x, y):  # x and y coordinates for interaction
        Turtle.__init__(self)

        # create Y slider
        self._color = [0, 0, 0]
        self.x = x
        self._color[x] = y
        self.color(self._color)
        self.speed(0)
        self.left(90)
        self.pu()
        self.goto(x, 0)
        self.pd()
        self.sety(1)
        self.pu()
        self.sety(y)
        self.pencolor("gray25")
        self.ondrag(self.shift)

    # set y shifter func
    def shift(self, y):
        self.sety(max(0, min(y, 1)))
        self._color[self.x] = self.ycor()
        self.fillcolor(self._color)

def main():
    global screen, a, b, c


    # # create triangle here
    # writer = Turtle()
    # writer.ht()
    # writer.forward(100)  # set base
    #
    # writer.left(135)  # change direction
    # writer.forward(142)  # set angle forward
    #
    # writer.left(135)  # change direction
    # writer.forward(100)  # go forward
    screen = Screen()
    screen.delay(0)
    screen.setworldcoordinates(-1, -0.3, 3, 1.3)

    a = trigY(0, .5)
    b = trigY(1, .5)
    c = trigY(2, .5)


    writer = Turtle()
    writer.ht()
    writer.pu()
    writer.goto(1, 1.15)
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()