# Simple Pong in Python 3 for Beginners
# Codebase from: http://christianthompson.com/sites/default/files/Pong/pong.py
# https://www.freecodecamp.org/news/python-projects-for-beginners/#pong-python-project
# By @TokyoEdTech

import turtle
import os

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("darkred")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 3
score_b = 3
score_c = 3
#location A(left) = -350; B(right) = 350; C(bottom) = -250
class Paddle:
	def __init__(self, speed, shape, color, paddle_width, paddle_length, start_x, start_y):
		paddle_a = turtle.Turtle()
		paddle_a.speed(speed)
		paddle_a.shape(shape)
		paddle_a.color(color)
		paddle_a.shapesize(stretch_wid=paddle_width,stretch_len=paddle_length)
		paddle_a.penup()
		paddle_a.goto(start_x, start_y)
#create paddle A - left
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
#paddle_a = Paddle(0, "square", "green", 5, 1, -350, 0)
#paddle_b = Paddle(0, "square", "red", 5, 1, 350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Paddle C 
paddle_c = turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("square")
paddle_c.color("green")
paddle_c.shapesize(stretch_wid=1, stretch_len=5)
paddle_c.penup()
paddle_c.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player L: 3  Player R: 3 Player B: 3", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def paddle_c_left():
    x = paddle_c.xcor()
    x += 40
    paddle_c.setx(x)

def paddle_c_right():
    x = paddle_c.xcor()
    x -= 40
    paddle_c.setx(x)

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_c_left, "n")
wn.onkeypress(paddle_c_right, "b")

# Main game loop
while True:
		wn.update()
		
		# Move the ball
		ball.setx(ball.xcor() + ball.dx)
		ball.sety(ball.ycor() + ball.dy)
	
		# Border checking
	
		# Top
		if ball.ycor() > 290:
				ball.sety(290)
				ball.dy *= -1
				os.system("afplay bounce.wav&")
			
		#BOTTOM
		elif ball.ycor() < -260:
				score_c -= 1
				pen.clear()
				pen.write("Player L: {}  Player R: {} Player B: {}".format(score_a, score_b, score_c), align="center", font=("Goudy Old Style", 24, "normal"))
				ball.goto(0, 0)
				ball.dy *= -1
			
	
		# Left and right
		if ball.xcor() > 350:  
				score_b -= 1
				pen.clear()
				pen.write("Player L: {}  Player R: {} Player B: {}".format(score_a, score_b, score_c), align="center", font=("Goudy Old Style", 24, "normal"))
				ball.goto(0, 0)
				ball.dx *= -1
	
		elif ball.xcor() < -350:
				score_a -= 1
				pen.clear()
				pen.write("Player L: {}  Player R: {} Player B: {}".format(score_a, score_b, score_c), align="center", font=("Goudy Old Style", 24, "normal"))
				ball.goto(0, 0)
				ball.dx *= -1
	
		# Paddle and ball collisions
		if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
				ball.dx *= -1 
				os.system("afplay bounce.wav&")
		
		if ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
				ball.dx *= -1
				os.system("afplay bounce.wav&")
	
		if ball.ycor() < -240 and ball.xcor() < paddle_c.xcor() + 50 and ball.xcor() > paddle_c.xcor() - 50:
				ball.dy *= -1
				os.system("afplay bounce.wav&")
		
		#check for winner
		if (score_a <= 0 and score_b <= 0):
			print("Player B Wins!")
			break
		elif (score_a <= 0 and score_c <= 0):
			print("Player R Wins!")
			break
		elif(score_b <= 0 and score_c <= 0):
			print("Player L wins!")
			break
