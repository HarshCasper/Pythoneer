import turtle
import time

# writing the labels for simulation
text=turtle.Turtle(visible=False)
text.up()
text.fd(300)
text.down()
text.color('red')
text.fd(30)
text.write("Trajectory of motion",font=("Ariel", 16, "normal"))
text.up()
text.back(30)
text.right(90)
text.fd(40)
text.left(90)
text.color('green')
text.down()
text.fd(30)
text.write("Radial Acceleration",font=("Ariel", 16, "normal"))
text.up()
text.back(30)
text.right(90)
text.fd(40)
text.left(90)
text.color('brown')
text.down()
text.fd(30)
text.write('Tangential acceleration',font=("Ariel", 16, "normal"))
text.up()
text.back(30)
text.right(90)
text.fd(40)
text.left(90)
text.color('black')
text.down()
text.fd(30)
text.write('Object in motion',font=("Ariel", 16, "normal"))


circle=turtle.Turtle(visible=False)
Turtle=turtle.Turtle(visible=False)
radial=turtle.Turtle(visible=False)
circle.speed(20)
Turtle.speed(20)
radial.speed(20)

#colors of turtles
circle.color('red')
radial.color('green')

#penwidth
radial.pensize(2)

for i in range(36):
    Turtle.circle(10)
    circle.left(10)
    circle.forward(15)
    time.sleep(0.1)
    Turtle.clear()
    Turtle.up()
    Turtle.left(10)
    Turtle.forward(15)
    Turtle.down()

# Turtle=turtle.Turtle(visible=False)
# Turtle.speed(20)


for i in range(36):
    Turtle.circle(10)
    time.sleep(0.1)
    circle.left(10)
    circle.forward(15)
    #radial and tangential acceleration
    if(i%4==0):
        radial.forward(30)
        radial.up()
        radial.back(30)
        radial.left(90)
        radial.down()
        radial.color('brown')
        radial.forward(30)
        radial.color('green')
        radial.up()
        radial.back(30)
        radial.right(90)
        radial.down()
        radial.color('blue')
        radial.circle(10)
        radial.color('green')
        radial.up()
        radial.left(10)
        radial.forward(15)
        radial.down()
    else:
        radial.up()
        radial.left(10)
        radial.forward(15)
        radial.down()

    #Erasing the circle for moving effects
    Turtle.clear()
    #External circle and the object
    Turtle.up()
    Turtle.left(10)
    Turtle.forward(15)
    Turtle.down()
time.sleep(1)

# Turtle.reset()
# radial.reset()
# circle.reset()
# text.reset()
turtle.Screen().clear()

# Pendulum motion

bar=turtle.Turtle(visible=False)
pen=turtle.Turtle(visible=False)

pen.speed(20)
bar.speed(20)

pen.color('red')
bar.color('red')

bar.fd(40)
bar.back(80)
pen.right(90)
def left(rounds):
 for i in range(rounds):
   pen.fd(120)
   pen.right(90)
   pen.fd(3)
   pen.circle(10)
   pen.back(3)
   pen.left(90)
   pen.back(120)
   pen.right(3)
   time.sleep(0.2)
   pen.clear()
def right(rounds):
 for j in range(rounds):
   pen.fd(120)
   pen.right(90)
   pen.fd(3)
   pen.circle(10)
   pen.back(3)
   pen.left(90)
   pen.back(120)
   pen.left(3)
   time.sleep(0.2)
   pen.clear()
m=13
for k in range(7):
    left(m)
    right(m)
    right(m)
    left(m)
    m-=4
pen.fd(120)
pen.right(90)
pen.fd(3)
pen.circle(10)
turtle.Screen().exitonclick()
