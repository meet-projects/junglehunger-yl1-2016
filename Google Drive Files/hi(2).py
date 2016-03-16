from turtle import *
from junglehunger.py import*
class Trampoline (Turtle):
	def __init__(self,dx,x_cor,y_cor,width,height):
		self.dx = dx
		self.x_cor = x_cor
		self.y_cor = y_cor
		self.goto(self.x_cor,self.y_cor)
		self.width = width
		self.height = height
	

	def move(self):
		self.goto(self.xcor()+self.dx,self.ycor())
		




t = Trampoline(0,0,-120,50,30)

def right():  #paddle
	global t
	t.dx=1
	t.move()
	t.dx=0

def left():    #paddle
	t.dx=-1
	t.move()
	t.dx=0


canvas.bind("<right>", right)
canvas.bind("<left>", left)
   


if (ball.r == t.xcor and ball.ycor()<= t.ycor+t.height/2):    #bounce
	ball.dx=-1
	ball.move()
elif (ball.r == t.width/2 and ball.ycor()<= t.ycor+t.height/2):
	ball.dx=-1
	ball.move()
else (ball.r == t.-width/2 and ball.ycor()<= t.ycor+t.height/2):
	ball.dx=-1
	ball.move()

 							


from turtle import *
from junglehunger.py import*
class Trampoline (Turtle):
	def __init__(self,dx,x_cor,y_cor,width,height):
		self.dx = dx
		self.x_cor = x_cor
		self.y_cor = y_cor
		self.goto(self.x_cor,self.y_cor)
		self.width = width
		self.height = height
	

	def move(self):
		self.goto(self.xcor()+self.dx,self.ycor())
		




t = Trampoline(0,0,-120,50,30)

def right():  #paddle
	global t
	t.dx=1
	t.move()
	t.dx=0

def left():    #paddle
	t.dx=-1
	t.move()
	t.dx=0


canvas.bind("<right>", right)
canvas.bind("<left>", left)
   


if (ball.r == t.xcor and ball.ycor()<= t.ycor+t.height/2):    #bounce
	ball.dx=-1
	ball.move()
elif (ball.r == t.width/2 and ball.ycor()<= t.ycor+t.height/2):
	ball.dx=-1
	ball.move()
else (ball.r == t.-width/2 and ball.ycor()<= t.ycor+t.height/2):
	ball.dx=-1
	ball.move()

 							



