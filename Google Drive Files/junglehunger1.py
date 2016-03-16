from turtle import *
from junglehunger import *
from hi import *

tracer(0)
ht()
canvas=getcanvas() # the canvas is the area that the turtle is moving (the white background)
CANVAS_WIDTH = canvas.winfo_width() # here we get canvas(screen) width
CANVAS_HEIGHT = canvas.winfo_height() # here we get the canvas(screen) height


lives=3
# This function returns the width of the screen
def get_screen_width():
	global CANVAS_WIDTH
	return int(CANVAS_WIDTH/2-10)

# This function returns the height of the screen
def get_screen_height():
	global CANVAS_HEIGHT
	return int(CANVAS_HEIGHT/2-5)

def borders(ball):
	global CANVAS_WIDTH
	global CANVAS_HEIGHT
	width = CANVAS_WIDTH
	height = CANVAS_HEIGHT
	x =ball.xcor()
	y = ball.ycor()
	if (x > width): #right border
		ball.dx=-ball.dx
	if (x < -width): #left border
		ball.dx=-ball.dx
	if (y > height): #top border
		ball.dy=-ball.dy
	if (y < -height): 
		lives=-1
		if (lives ==0):
			turtle.bye
    

ball1= Ball(1,1,.1,.1,2,3,2,"square")
ball1.penup()

t = Trampoline(0,0,-220,50,30)
def right(event):  #paddle
	global t
	t.dx=1
	t.move()
	t.dx=0

def left(event):    #paddle
	t.dx=-1
	t.move()
	t.dx=0


canvas.bind("<Right>", right)
canvas.bind("<Left>", left)
   

while True:
	ball1.move()
	t.move()
	getscreen().update()
