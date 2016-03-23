from turtle import *
from random import randint
from junglehunger import *
from hi import *
from Classes import *
tracer(0)
ht()

fruits_list = []

canvas=getcanvas() # the canvas is the area that the turtle is moving (the white background)
CANVAS_WIDTH = canvas.winfo_width() # here we get canvas(screen) width
CANVAS_HEIGHT = canvas.winfo_height() # here we get the canvas(screen) height
screen = getscreen()
#screen.register_shape("monkey.gif")


bgpic('jungle.gif')


screen.register_shape("banana.gif")
screen.register_shape("apple.gif")
screen.register_shape("grapes.gif")
screen.register_shape("orange.gif")
screen.register_shape("pineapple.gif")
screen.register_shape("strawberry.gif")

fruits = ["apple.gif", "banana.gif", "grapes.gif", "orange.gif", "pineapple.gif", "strawberry.gif",]

#fruit1 = Fruit(fruits[randint(0,5)], 0 ,0 , 10, 10)

j = 1
changeX = 0
while(j <= 3):
	dx = 0
	i = 1
	while ( i < 20 ):
		temp_fruit = Fruit(fruits[randint(0,5)],-320 + dx ,250 - changeX, 10, 10)
		fruits_list.append(temp_fruit)
		dx = dx + 35
		i+=1
	changeX+=50
	j+=1
penup()
goto(500,500)

def collided(ball1,obj):
	#object measurements
	otop= obj.ycor()+obj.height/2
	obottom= obj.ycor()-obj.height/2
	oright= obj.xcor()+obj.width/2
	oleft= obj.xcor()-obj.width/2
	
	#ball measurements
	btop= ball1.ycor()+ball1.r
	bbottom= ball1.ycor()-ball1.r
	bright= ball1.xcor()+ball1.r
	bleft= ball1.xcor()-ball1.r
	
	if btop>=obottom and otop>=bbottom and bright>=oleft and oright>=bleft:
		return True
	else:
		return False

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
	width = get_screen_width()
	height = get_screen_height()
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
			exit()
    

ball1= Ball(1,0.1,0.1,2,3,2,"square")

t = Trampoline(0,1,-230,2,1)
def right(event):  #paddle
	global t
	print("right")
	t.dx=20
	t.move()
	t.dx=0

def left(event):    #paddle
	global t
	print("left")
	t.dx=-20
	t.move()
	t.dx=0

canvas.bind("<Right>", right)
canvas.bind("<Left>", left)
screen.listen()


   
print (len(fruits_list))
while True:
	ball1.move()
	t.move()
	borders(ball1)
	if (collided(ball1,t)):
		ball1.dy*=-1
	for f in fruits_list:
		if(collided(ball1,f)):
			ball1.dy*=-1
			f.hideturtle()
			fruits_list.remove(f)
	screen.update()
