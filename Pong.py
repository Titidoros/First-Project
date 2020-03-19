import turtle

Wi = 800
He = 400
V = 5


speed = 0.2

wn = turtle.Screen()
wn.title("Pong by Titi")
wn.bgcolor("light blue")
wn.setup(width=Wi, height=He)
wn.tracer(0)

#racket A
racket_a = turtle.Turtle()
racket_a.speed(0)
racket_a.shape("square")
racket_a.color("brown")
racket_a.shapesize(stretch_wid=5 ,stretch_len=1)
racket_a.penup()
racket_a.goto(Wi/-2+50, 0)

#paddle B
racket_b = turtle.Turtle()
racket_b.speed(0)
racket_b.shape("square")
racket_b.color("brown")
racket_b.shapesize(stretch_wid=5 ,stretch_len=1)
racket_b.penup()
racket_b.goto(Wi/2-50, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("dark red")
ball.penup()
ball.goto(0, 0)
ball.dx = speed
ball.dy = speed

#scoring system
# score
score_a = 0
score_b = 0

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0, He/4)
pen.write("Joueur 1: 0 Joueur 2: 0", align="center", font=("Courier", 24, "normal"))

# Function

def racket_a_up():
    y = racket_a.ycor()
    y += 20
    racket_a.sety(y)

def racket_a_down():
    y = racket_a.ycor()
    y -= 20
    racket_a.sety(y)

def racket_b_up():
    y = racket_b.ycor()
    y += 20
    racket_b.sety(y)

def racket_b_down():
    y = racket_b.ycor()
    y -= 20
    racket_b.sety(y)

#keyboard binding
wn.listen()
wn.onkeypress(racket_a_up, "z")
wn.onkeypress(racket_a_down, "s")
wn.onkeypress(racket_b_up, "Up")
wn.onkeypress(racket_b_down, "Down")


while True:
    wn.update()
    """ if score_a == V or score_b == V :
        break
            wn.update()

        if score_a > score_b:
            pen.write("Joueur 1 gagne!", align="center", font=("Courier", 24, "normal"))
        else:
            pen.write("Joueur 2 gagne!", align="center", font=("Courier", 24, "normal")) """

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # bords de l'écran
    
    Bd = Wi/2-10
    Bg = -Wi/2+10
    Bh = He/2-10
    Bb = -He/2+10

    if ball.ycor() > Bh:
        ball.sety(Bh)
        ball.dy *= -1

    if ball.ycor() < Bb:
        ball.sety(Bb)
        ball.dy *= -1
        

    if ball.xcor() > Bd:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Joueur 1: {} Joueur 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < Bg:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Joueur 1: {} Joueur 2: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    """ if score_a == V :
        pen.clear()
        pen.write("Joueur 1 gagne!", align="center", font=("Courier", 24, "normal"))

    if score_b == V :
        pen.clear()
        pen.write("Joueur 2 gagne!", align="center", font=("Courier", 24, "normal")) """
    
    # racket et ballon collision

    if (ball.xcor() > Wi/2-60 and ball.xcor() < Wi/2-50) and (ball.ycor() < racket_b.ycor() + 40 and ball.ycor() > racket_b.ycor() -40):
        ball.setx(Wi/2-60)
        ball.dx *= -1

    if (ball.xcor() < Wi/-2+60 and ball.xcor() > Wi/-2+50) and (ball.ycor() < racket_a.ycor() + 40 and ball.ycor() > racket_a.ycor() -40):
        ball.setx(Wi/-2+60)
        ball.dx *= -1

   
