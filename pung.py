import turtle
import winsound

wn = turtle.Screen()
wn.title("pong by Abhijith")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) # its actualy stop window from updating

# paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#pen Scooring system

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("player A : 0 "  " player B : 0", align="center", font=("courier", 24, "normal"))
#score
score_a = 0
score_b = 0


# __________Funtions___________
     # paddle a

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

    # paddle b

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



# --------keyboard binding--------

wn.listen()

#--------paddle a_______
wn.onkeypress(paddle_a_up, "w")

wn.onkeypress(paddle_a_down, "s")

#_________paddle b_______
wn.onkeypress(paddle_b_up, "Up")

wn.onkeypress(paddle_b_down, "Down")





# Mani game loop
while True:
    wn.update()

    # Ball move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('ping.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('ping.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

    if ball.xcor() > 390:
         ball.goto(0, 0)
         ball.dx *= -1
         score_a += 1
         pen.clear()
         pen.write("player A : {} "  " player B : {}".format(score_a, score_b), align="center", font=("courier", 24, "normal"))

    if ball.xcor() < -390:
         ball.goto(0, 0)
         ball.dx *= -1
         score_b += 1
         pen.clear()
         pen.write("player A : {} "  " player B : {}".format(score_a, score_b), align="center",  font=("courier", 24, "normal"))

    #  paddale and ball collision
    if(ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('ping.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('ping.wav', winsound.SND_ALIAS | winsound.SND_ASYNC)
