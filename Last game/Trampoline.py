from turtle import *
screen = getscreen()
screen.register_shape("trampoline.gif")
class Trampoline (Turtle):
	def __init__(self,dx,xcor,ycor,width,height):
		Turtle.__init__(self)
		self.dx = dx
		self.penup()
		self.goto(xcor,ycor)
		self.width = width*20
		self.height = height*20
		self.shape("trampoline.gif")
		self.shapesize(height,width,2)

	def move(self):
		self.goto(self.xcor()+self.dx,self.ycor())
 							

