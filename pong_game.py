
import turtle
window=turtle.Screen() # creates a screen
window.title("Pong Project") # title of screen window
window.bgcolor("black") # color of screen
window.setup(width=800, height=600) # Sets proportion of game
window.tracer(0) # stops window from updating to manually update it

#Score
score_a=0
score_b=0

paddle_a=turtle.Turtle()
paddle_a.speed(0) # speed of animation speed=0 is max
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0) #left side of the screen
#
#
# # Paddle B
#
paddle_b=turtle.Turtle()
paddle_b.speed(0) # speed of animation speed=0 is max
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0) #left side of the screen


# Ball

ball=turtle.Turtle()
ball.speed(0) # speed of animation speed=0 is max
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0) #left side of the screen

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-20,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24,"normal"))

#ball movement

ball.dx=4
ball.dy=4

# Function
def paddle_a_up():
    y=paddle_a.ycor()
    y+=40
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=40
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=40
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=40
    paddle_b.sety(y)


#Keyboard binding
window.listen()
window.onkeypress(paddle_a_up,"w")
window.onkeypress(paddle_a_down,"s")
window.onkeypress(paddle_b_up,"p")
window.onkeypress(paddle_b_down,";")



while True: # Main game loop
    window.update()

    #move the Ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1 #reverses direction of ball

    if ball.ycor()<-280:
        ball.sety(-280)
        ball.dy *= -1 #reverses direction of ball

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.color("white")
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx *= -1
        ball.color("white")
        score_b+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"normal"))


    # Paddle and ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < (paddle_b.ycor()+50) and (ball.ycor()>paddle_b.ycor()-50)):
        ball.setx(340)
        ball.dx *= -1
        ball.color("red")

    if ball.xcor() < -340 and ball.xcor()> -350 and (ball.ycor() < (paddle_a.ycor()+50) and (ball.ycor()>paddle_a.ycor()-50)):
        ball.setx(-340)
        ball.dx *= -1
        ball.color("blue")
#testing
