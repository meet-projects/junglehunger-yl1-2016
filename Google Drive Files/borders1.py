from turtle import *
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

def borders(monkey):
	global CANVAS_WIDTH
	global CANVAS_HEIGHT
	width = CANVAS_WIDTH
	height = CANVAS_HEIGHT
	x = monkey.xcor()
	y = monkey.ycor()
	if (x > width): #right border
		monkey.dx=-monkey.dx
	if (x < -width): #left border
		monkey.dx=-monkey.dx
	if (y > height): #top border
		monkey.dy=-mpnkey.dy
	if (y < -height): 
		lives=-1
		if (lives ==0):
			turtle.bye

