def collided(ball,obj):
	#object measurements
	otop= obj.ycor()+obj.height/2
	obottom= obj.ycor()-obj.height/2
	oright= obj.xcor()+obj.width/2
	oleft= obj.xcor()-obj.width/2
	
	#ball measurements
	btop= ball.ycor()+ball.r
	bbottom= ball.ycor()-ball.r
	bright= ball.xcor()+ball.r
	bleft= ball.xcor()-ball.r
	
	if btop>=obottom and otop<=bbottom:
		return True
	elif bright>=oleft and oleft<=bright:
		return True
	else:
		return False
	
