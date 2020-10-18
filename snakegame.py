import turtle
import time
import random

delay=0.5
wn=turtle.Screen()
wn.bgcolor("orange")
wn.setup(width=600,height=600)
wn.title("SNAKE GAME")
wn.tracer(0)#turns off the animation on the screen


#snake head:
head=turtle.Turtle()
head.shape("square")
head.color("red")
head.goto(0,0)
head.direction='stop'
head.speed(0)
head.penup()#so that turtle does not draw any line when it moves

# food:
food=turtle.Turtle()
food.penup()
food.shape("circle")
food.color("black")
food.shapesize(0.5,0.5)
food.goto(0,100)
food.speed(0)

#pen:
pen=turtle.Turtle()
pen.shape("square")
pen.color("black")
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0  High Score:0",align="center",font=("Courier",25,"normal"))


segments=[]
score=0
high_score=0


def go_up():
	head.direction="up"
def go_down():
	head.direction="down"
def go_right():
	head.direction="right"
def go_left():
	head.direction="left"


def move():
	if head.direction=="up":
		y=head.ycor()
		head.sety(y+20)
	if head.direction=="down":
		y=head.ycor()
		head.sety(y-20)
	if head.direction=="right":
		x=head.xcor()
		head.setx(x+20)
	if head.direction=="left":
		x=head.xcor()
		head.setx(x-20)
#key board bindings
wn.listen()
wn.onkeypress(go_up,"u")
wn.onkeypress(go_down,"d")
wn.onkeypress(go_left,"l")
wn.onkeypress(go_right,"r")


while True:
	wn.update()


	if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
		head.goto(0,0)
		head.direction="stop"
		time.sleep(1)
		for ele in segments:
			ele.goto(1000,1000)
		segments.clear()
		#reset the score to 0 as it has collided with the wall
		score=0
		pen.clear()#clears the screen as beginning would be 0,0 and they would change
		pen.write("Score: {}  High Score:{}".format(score,high_score),align="center",font=("Courier",25,"normal"))



	if head.distance(food)<20:#in turtle,each square measures 20 pixels ie,if they touch distance would be lesss than 20
		#move food to random spot
		x=random.randint(-290,290)#so that food wont go off the screen
		y=random.randint(-290,290)
		food.goto(x,y)

		#adding body to snake:
		new_segment=turtle.Turtle()
		new_segment.color("black")
		new_segment.penup()
		new_segment.speed(0)
		new_segment.shape("square")
		segments.append(new_segment)
		#x1=new_segment.xcor()
		#y1=new_segment.ycor()
		#x1=head.xcor()
		#y1=head.ycor()
		#new_segment.goto(x1,y1)

		#adding score:
		score += 10

		#check for the high score:
		if score > high_score:
			high_score = score
        #writing score:
		pen.clear()#clears the screen as beginning would be 0,0 and they would change
		pen.write("Score: {}  High Score:{}".format(score,high_score),align="center",font=("Courier",25,"normal"))



	for index in range(len(segments)-1,0,-1):#every time the while"true" loop runs,lenght of list-segment increases by 1 
		x1=segments[index-1].xcor()#by 1.first time the lenght would be 1 and it goes to if statement not inside
		y1=segments[index-1].ycor()#the for loop.2nd time 2 segments would be there and it already knows the pos of 
		segments[index].goto(x1,y1)#the first one.3rd time 3 segemnts would be there and 3rd would know the pos of 2nd
	'''for i in range(1,len(segments)):
		x1=segments[i-1].xcor()
		y1=segments[i-1].ycor()
		segments[i].goto(x1,y1)'''
	if len(segments)>0:
		x2=head.xcor()
		y2=head.ycor()
		segments[0].goto(x2,y2)
	'''for index in range(len(segments)-1,0,-1):
		x1=segments[index-1].xcor()
		y1=segments[index-1].ycor()
		segments[index].goto(x1,y1)'''

	'''for i in range(1,len(segments)):
		x1=segments[i-1].xcor()
		y1=segments[i-1].ycor()
		segments[i].goto(x1,y1)'''


	move()


	#to check for body collisions after being moved:
	'''for segment in segments:
		if head.distance(segment)<20:
			time.sleep(1)
			head.goto(0,0)
			head.direction="stop"
		for segment in segments:#deletes the segments,makes them disappear
			segment.goto(1000,1000)
		segments.clear()#clears the segments'''

	time.sleep(delay)
wn.mainloop()

#Goal : tO implement snake game
#The user has to direct the snake in collecting it's food without letting th =e snake touch the boundaries/walls
#lang used: python
#packages used: turtle, time, random






