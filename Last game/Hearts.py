from turtle import *

class Heart(Turtle):
	def __init__(self,picture ,x ,y):
		Turtle.__init__(self)
		self.penup()
		self.goto(x,y)
		self.shape(picture)


