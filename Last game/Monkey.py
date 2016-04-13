from turtle import *
screen = getscreen()
screen.register_shape("monkey.gif")
class Ball(Turtle):
    def __init__(self,r ,dx,dy,x,y,lives,shape):
        Turtle.__init__(self)
        self.dx= dx
        self.dy= dy
        self.lives= lives
        self.pu()
        self.goto(x,y)
        self.r=r
        self.shape("monkey.gif")

    def move(self):
        self.goto(self.xcor()+self.dx,self.ycor()+self.dy)

