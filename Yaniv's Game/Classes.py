from turtle import *

class Fruit(Turtle):
	def __init__(self,picture ,x ,y , width, height):
		Turtle.__init__(self)
		self.penup()
		self.goto(x,y)
		self.shape(picture)
		self.width = width
		self.height = height
		

