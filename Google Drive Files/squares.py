import turtle
import random
import time

turtle.pendown()
#turtle.goto (0,0)
turtle.penup()
#turtle.goto (-200,0)
turtle.shape ("square")
turtle.goto (-200,200)
turtle.penup()

turtle.pendown()
turtle.penup()
turtle.shape ("square")
turtle.goto (-150,200)
turtle.pendown()
time.sleep(3)

#cells=[]
#user_cell= {"radius": 20, "x": 50, "y": -50, "dy": 1, "dx": 2, "color": "black"}
#user_cell1= meet.create_cell(user_cell)
#cells.append(user_cell1)
#z=0
#while(z<20):
#	ball1= {"radius": random.randint(10,30), "x":random.randint(-50,100), "y":random.randint(30,100), "dy":random.random(), "dx": random.random(), "color": colors[random.randint(0, len(colors)-1)]}
#	circle1= meet.create_cell(ball1)
#	cells.append(circle1)
#	z+=1
#playing=True
