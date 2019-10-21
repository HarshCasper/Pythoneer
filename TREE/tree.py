import turtle
import random 
import math 
turtle.screensize(900,900)
c = (0.1,0.01,0.3)
turtle.bgcolor(c)
a = turtle.Turtle ("classic",1000,False) 
b = turtle.Turtle ("classic",1000,False) 
b.up()
b.goto(-180,200)
b.write("The Power of Recursion!!\n FRACTALS --> Order in Chaos!!",False,"center",("Arial",20,"normal"))
b.goto(180,180)
b.write("\n\n")
b.write("\n\nJust run the program,\n come and watch after\n 15 mins!!",False,"center",("Arial",20,"normal"))
a.left(90)
a.up()
a.goto(0,-200)
a.down()
a.speed(0)
def fractal (a,length ,size,angle,t) : 
    if (size<2):
        tup = (1-t,1-t,1-t)
        tup2= (1-t,1-t,1-t)
        k = random.randint(1,100)
        if (k < 45):
            a.pencolor(tup2)
        elif(k > 45 & k <= 75) :
            a.pencolor(tup2)
        else : 
            a.pencolor(tup)
    
        a.pensize(1.5)
        a.fd(5)
        return
    
    a.speed(0)
    tup2 = (1-t,t,1-t)
    a.begin_fill()
    k = random.randint(1,100)
    if (k < 70):
        a.pencolor(tup2)
    else : 
        a.pencolor(tup2)
    a.pensize (size) 
    a.fd(length)
    a.end_fill()
    flag = False
    aLeft = turtle.Turtle('classic',1000,False)
    aLeft.speed(0)
    
    aLeft.up()
    aRight= turtle.Turtle('classic',1000,False)
    aRight.speed(0)
    aRight.up() 
    aLeft.goto(a.xcor(),a.ycor())
    aRight.goto(a.xcor(),a.ycor())
    aLeft.down()
    aRight.down() 
    aLeft.left(angle+45)
    aRight.left(angle-45)
   
    
    fractal(aLeft,length*0.75,size*0.75,angle+45,t+0.05)
    fractal(aRight,length*0.75,size*0.75,angle-45,t+0.05)
fractal(a,100,40,90,0.1) 
b.clear()   
input()
