from random import randint
from turtle import *
from Classes import Fruit
'''
canvas = getcanvas()
CANVAS_WIDTH = canvas.winfo_width()
CANVAS_HEIGHT = canvas.winfo_height()
'''
screen = getscreen()

screen.register_shape("banana.gif")
screen.register_shape("apple.gif")
screen.register_shape("grapes.gif")
screen.register_shape("orange.gif")
screen.register_shape("pineapple.gif")
screen.register_shape("strawberry.gif")

fruits = ["apple.gif", "banana.gif", "grapes.gif", "orange.gif", "pineapple.gif", "strawberry.gif",]

#fruit1 = Fruit(fruits[randint(0,5)], 0 ,0 , 10, 10)
x = 1
dx = 0
while ( x < 80 ):
	if (x < 20):
		Fruit(fruits[randint(0,5)],-320 + dx ,200 , 10, 10)
		dx = dx + 35
	if ( 20 <= x <= 40):
#Didn't finish here

while True:
	pass

