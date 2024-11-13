import turtle
turtle.speed(5)
turtle.penup()
turtle.goto(-450,-200)
turtle.pendown()
turtle.title("House")

#Pen Details
turtle.pen(pencolor="black",pensize=2)

#Base
turtle.forward(900)
turtle.backward(250)
turtle.left(90)

#Walls
turtle.color("blue")
turtle.begin_fill()
turtle.forward(200)
turtle.left(90)
turtle.forward(3)
turtle.right(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(5)
turtle.right(90)
turtle.forward(5)

turtle.left(90)
turtle.forward(150)
turtle.left(120)
turtle.forward(25)
turtle.right(120)
turtle.forward(20)
turtle.left(90)
turtle.forward(187)
turtle.end_fill()

turtle.right(90)
turtle.forward(175)

#Pillars
turtle.speed(5)
turtle.color("gray")
turtle.begin_fill()
turtle.right(90)
turtle.forward(187)
turtle.left(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(187)
turtle.end_fill()

turtle.color("purple")
turtle.left(90)
turtle.forward(173)

turtle.color("orange")
turtle.begin_fill()
turtle.left(90)
turtle.forward(187)
turtle.right(90)
turtle.forward(5)
turtle.right(90)
turtle.forward(187)
turtle.end_fill()

turtle.backward(187)
turtle.right(90)
turtle.forward(2)
turtle.forward(180)

#Walls 2
turtle.speed(5)
turtle.color("red")
turtle.begin_fill()
turtle.forward(192)
turtle.left(90)
turtle.forward(187)
turtle.left(90)
turtle.forward(193)
turtle.end_fill()
turtle.left(90)
turtle.forward(187)

#Pillars 2
turtle.speed(5)
turtle.color("gray")
turtle.begin_fill()
turtle.left(90)
turtle.forward(195)
turtle.left(90)
turtle.forward(187)
turtle.right(90)
turtle.forward(7)
turtle.right(90)
turtle.forward(187)
turtle.left(90)
turtle.forward(3)
turtle.right(90)
turtle.forward(5)
turtle.left(90)
turtle.forward(3)
turtle.right(90)
turtle.forward(7)
turtle.right(90)
turtle.forward(188)
turtle.right(135)
turtle.forward(16)
turtle.end_fill()
turtle.right(225)

#Roof
turtle.speed(5)
turtle.color("black")
turtle.begin_fill()
turtle.right(-45)
turtle.forward(180)
turtle.right(94)
turtle.forward(170)
turtle.right(131)
turtle.forward(240)
turtle.end_fill()

#Roof 2
turtle.speed(5)
turtle.begin_fill()
turtle.right(-225)
turtle.forward(330)
turtle.right(94)
turtle.forward(285)
turtle.right(131)
turtle.forward(300)
turtle.end_fill()

#Roof 3
turtle.speed(5)
turtle.left(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(310)

turtle.begin_fill()
turtle.right(-225)
turtle.forward(130)
turtle.right(45)
turtle.forward(200)
turtle.right(-225)
turtle.forward(130)
turtle.end_fill()

#Trims
turtle.speed(5)
turtle.color("blue")
turtle.right(45)
turtle.forward(200)
turtle.right(-225)
turtle.forward(130)
turtle.right(45)
turtle.forward(195)
turtle.right(-45)
turtle.forward(190)
turtle.right(94)
turtle.forward(287)
turtle.right(-229)
turtle.forward(195)
turtle.right(225)
turtle.forward(28)
turtle.right(-225)
turtle.forward(250)
turtle.right(135)
turtle.forward(180)
turtle.right(91)
turtle.forward(170)

turtle.right(134)
turtle.forward(240)

#Windows
turtle.speed(5)
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
turtle.forward(55)
turtle.right(90)
turtle.forward(130)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(130)
turtle.end_fill()

#Window Frame
turtle.speed(10)
turtle.color("black")
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(130)
turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(130)

turtle.right(90)
turtle.forward(55)
turtle.right(90)
turtle.forward(65)
turtle.right(90)
turtle.forward(55)

turtle.right(90)
turtle.forward(65)
turtle.right(90)
turtle.forward(27.5)
turtle.right(90)
turtle.forward(130)

#Door
turtle.color("black")
turtle.penup()
turtle.left(90)
turtle.forward(115)
turtle.left(90)
turtle.forward(225)
turtle.pendown()

turtle.begin_fill()
turtle.left(90)
turtle.forward(135)
turtle.right(90)
turtle.forward(65)
turtle.right(90)
turtle.forward(135)
turtle.end_fill()

#Window 2
turtle.penup()
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(100)
turtle.pendown()

turtle.color("pink")
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(95)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(95)
turtle.end_fill()

#Window Frame
turtle.color("black")
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(95)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(95)

turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(95)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(47.5)
turtle.right(90)
turtle.forward(50)

turtle.hideturtle()


turtle.exitonclick() 
turtle.exitonclick() 