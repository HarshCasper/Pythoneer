import turtle


def main():
    initTurtle()
    drawSquare()
    drawRectangle()
    drawCircle()
    drawStar()

######################################################

def initTurtle():
    turtle.shape("turtle")
    turtle.bgcolor("#87CEEB")

######################################################

def drawSquare():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.reset()

######################################################

def drawRectangle():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(60)
    turtle.reset()

######################################################

def drawCircle():
    turtle.circle(90)
    turtle.reset()

######################################################

def drawTriangle():
    turtle.left(180)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.right(120)
    turtle.forward(100)
    turtle.reset()

######################################################

def drawStar():
    turtle.color('red', 'yellow')
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()
    turtle.exitonclick()

######################################################

def drawOlympicLogo(radius):
    positions = [(60, 0, 'blue'), (-60, 0, 'purple'),
                 (120, 60, 'red'), (0, 60, 'yellow'), (-120, 60, 'green')]

    for position in positions:
        drawOlympicCircle(position[0], position[1], position[2], radius)

######################################################

def drawOlympicCircle(x, y, color, radius):
    turtle.pensize(10)
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)

######################################################

def drawSquareLoop():
    for num in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.reset()

######################################################

if __name__ == '__main__':
    main()
