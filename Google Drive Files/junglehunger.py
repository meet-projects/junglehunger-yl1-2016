from turtle import *

class Ball(Turtle):
    def __init__(self,width,height,dx,dy,x,y,lives,shape):
        Turtle.__init__(self)
        self.dx= dx
        self.dy= dy
        self.width= width
        self.height= height
        self.lives= lives
        self.goto(x,y)
        self.shape("circle")

    def move(self):
        self.goto(self.xcor()+self.dx,self.ycor()+self.dy)

