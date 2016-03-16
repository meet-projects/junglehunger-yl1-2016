from turtle import *
class Trampoline (Turtle):
	def __init__(self,dx,x_cor,y_cor,width,height):
		self.dx = dx
		self.x_cor = x_cor
		self.y_cor = y_cor
		self.goto(self.x_cor,self.y_cor)
		self.width = width
	

	def move(self):
		self.goto(self.xcor()+self.dx,self.ycor())
		




t = Trampoline(0,0,-120,50,30)

	



