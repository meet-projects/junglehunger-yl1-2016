from random import randint
from turtle import *
from Classes import Fruit
'''
canvas = getcanvas()
CANVAS_WIDTH = canvas.winfo_width()
CANVAS_HEIGHT = canvas.winfo_height()
'''
tracer(0)
screen = getscreen()

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
		Fruit(fruits[randint(0,5)],-320 + dx ,250 - changeX, 10, 10)
		dx = dx + 35
		i+=1
	changeX+=50
	j+=1
penup()
goto(500,500)
while True:
	screen.update()
