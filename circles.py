import turtle 
from itertools import cycle
turtle.bgcolor('black')
colors = cycle(['red','orange','yellow','green','blue','purple'])   
circle = turtle.Turtle() 
circle.speed(500) 
 
def draw_circle2(r = 70): # function for the second circle so it can be implemented in an infinite loop
	while True:
		for x in range (8): 
			circle.pensize(2)
			circle.pencolor(next(colors))
			circle.circle(r) 
			circle.left(45)

		r=r+20		
		

def draw_circle(r = 50):

	for i in range (8): # rember i in for loop start as i = 0
		circle.pensize(2)
		circle.pencolor(next(colors))
		circle.circle(r) 
		circle.left(45)
		if i == 7:
		 	draw_circle2()

def loop():		# loop so you can draw continuos circles
	while True :
		draw_circle()
loop()
turtle.done()



# COMMENTS
# circle.pencolor(next(colors))
# turtle.pencolor(next(colors)) # change of the colour every time use the array in line 5
# rember i in for loop start as i = 0
# r means the radius of the circle