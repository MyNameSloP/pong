import turtle
import time

wn = turtle.Screen()
wn.title("Pong par Louis ALEXIS")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0
score_c = 1
u = False
n = 165
m = 20

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.22
ball.dy = 0.22

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Louis: 0 Random: 0"" \!/ Combo Score:", align="center", font=("Courier", 20, "normal"))

# Pen Pause
pen_pause = turtle.Turtle()
pen_pause.speed(0)
pen_pause.color("black")
pen_pause.penup()
pen_pause.hideturtle()
pen_pause.goto(0, -150)

# Paddle_mid
paddle_mid = turtle.Turtle()
paddle_mid.speed(0)
paddle_mid.shape("square")
paddle_mid.color("black")
paddle_mid.shapesize(stretch_wid=4.5,stretch_len=0.7)
paddle_mid.penup()
paddle_mid.goto(0,0)

# Function
def paddle_a_up():
    y= paddle_a.ycor()
    y += m
    paddle_a.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    y -= m
    paddle_a.sety(y)

def paddle_b_up():
    y= paddle_b.ycor()
    y += m
    paddle_b.sety(y)

def paddle_b_down():
    y= paddle_b.ycor()
    y -= m
    paddle_b.sety(y)

def pause():
    score_t = 5
    wn.bgcolor("grey")
    for i in range(5):
        pen_pause.write("EN PAUSE: {} ".format(score_t), align="center", font=("Courier", 54, "normal"))
        time.sleep(1)
        pen_pause.clear()
        score_t -= 1
    wn.bgcolor("black")

def longue_pause():
    score_longue_pause = 30
    wn.bgcolor("grey")
    for i in range(30):
        pen_pause.write("EN PAUSE: {} ".format(score_longue_pause), align="center", font=("Courier", 54, "normal"))
        time.sleep(1)
        pen_pause.clear()
        score_longue_pause -= 1
    wn.bgcolor("black")
# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_a_up,"z")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")
wn.onkeypress(pause, "space")
wn.onkeypress(longue_pause, "n")


# Main Game Loop 
while True:
    wn.update()

    # Move The Ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Paddle Border Checking
    if (paddle_a.ycor() + 25 > 300):
        paddle_a.sety(260)
    if (paddle_a.ycor() - 25 < -300):
        paddle_a.sety(-260)

    if (paddle_b.ycor() + 25 > 300):
        paddle_b.sety(260)
    if (paddle_b.ycor() - 25 < -300):
        paddle_b.sety(-260)

    # Ball Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1        

    if ball.xcor() > 390:
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        m += 2
        ball.dx += 0.005
        ball.dy += 0.005
        ball.dx *= -1
        score_a += 1
        score_c += 9
        pen.clear()
        pen.write("Louis: {} Random: {} \!/ Combo Score: {} ".format(score_a, score_b, score_c), align="center", font=("Courier", 20, "normal"))
        n *= -1
        if ( u == True):
            ball.goto(0,n)
            time.sleep(1)
        else:
            ball.goto(0,0)
            time.sleep(1)
    
    if ball.xcor() < -390:
        paddle_a.goto(-350,0)
        paddle_b.goto(350,0)
        m += 2
        ball.dx += 0.005
        ball.dy += 0.005
        ball.dx *= -1
        score_b += 1
        score_c += 9
        pen.clear()
        pen.write("Louis: {} Random: {} \!/ Combo Score: {} ".format(score_a, score_b, score_c), align="center", font=("Courier", 20, "normal"))
        n *= -1
        if ( u == True):
            ball.setpos(0,n)
            time.sleep(1)
        else:
            ball.setpos(0,0)
            time.sleep(1)

    # Paddle and Ball Colisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 80 and ball.ycor() > paddle_b.ycor() - 80):
        ball.sety(ball.ycor())
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 80 and ball.ycor() > paddle_a.ycor() - 80):
        ball.sety(ball.ycor())
        ball.dx *= -1

    # Ball Turning
    if (score_a + score_b > 4.9):
        ball.shape("circle")

    # Paddle Mid Colisions And Activation
    if (score_a + score_b > 9.9):
        u = True
        paddle_mid.color("blue")
        if (ball.xcor() > -7 and ball.xcor() < 7) and (ball.ycor() < 55 and ball.ycor() > -55):
            ball.dx *= -1
        if (ball.xcor() > -7 and ball.xcor() < 7) and ((ball.ycor() < 55 or ball.ycor() > -55)):
            ball.dy *= 1

    # Color Blue
    if (score_a + score_b > 6.9):
        ball.color("blue")
        paddle_a.color("blue")
        paddle_b.color("blue")

    # Color Red
    if (score_a + score_b > 9.9):
        ball.color("red")
        paddle_a.color("red")
        paddle_b.color("red")

    # Color Green Bg
    if (score_a + score_b > 14.9):
        ball.color("orange")
        paddle_a.color("orange")
        paddle_b.color("orange")
        paddle_mid.color("red")