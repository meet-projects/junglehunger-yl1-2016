def lives
	lives=3
def borders(monkey):
	width = #get width
	height = #get height
	x = monkey.xcor()
	y = monkey.ycor()

	if (x > width): #right border
		monkey.set_dx(-cell.get_dx())
	if (x < -width): #left border
		monkey.set_dx(-cell.get_dx())
	if (y > height): #top border
		monkey.set_dy(-cell.get_dy())
	if (y < -height): 
		lives=-1
		if (lives ==0):
			turtle.bye
		
