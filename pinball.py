import turtle
w=turtle.Screen()
w.title("pinball")
w.bgcolor("black")
w.setup(width=800,height=600)
w.tracer(0)
a=turtle.Turtle()
a.speed(0)
a.shape("square")
a.color("white")
a.shapesize(stretch_wid=5,stretch_len=1)
a.penup()
a.goto(-350,0)
b=turtle.Turtle()
b.shape("square")
b.color("white")
b.speed(0)
b.shapesize(stretch_wid=5,stretch_len=1)
b.penup()
b.goto(350,0)
c=turtle.Turtle()
c.shape("square")
c.color("white")
c.penup()
c.shapesize(stretch_wid=2,stretch_len=2)
c.speed(0)
c.goto(0,0)
dx=0.1
dy=0.1
def moveup_a():
	ay=a.ycor()
	ay+=20
	a.sety(ay)
def movedown_b():
	by=b.ycor()
	by-=20
	b.sety(by)
def movedown_a():
	ay1=a.ycor()
	ay1-=20
	a.sety(ay1)
def moveup_b():
	by1=b.ycor()
	by1+=20
	b.sety(by1)
w.listen()
w.onkeypress(moveup_a,'w')
w.onkeypress(movedown_b,"d")
w.onkeypress(movedown_a,'b')
w.onkeypress(moveup_b,'r')
while True:#maingame loop
	w.update()#everytime loop runs,updates the screen
	#making the ball move
	c.sety(c.ycor()+dy)
	c.setx(c.xcor()+dx)
	#checking border conditions
	if c.ycor()>290:
		c.sety(290)
		dy*=-1
	if c.xcor()>390:
		c.setx(390)
		dx*=-1
	if c.ycor()<-290:
		c.sety(-290)
		dy*=-1
	if c.xcor()<-390:
		c.setx(-390)
		dx*=-1
	if (340<c.xcor()<350) and (b.ycor()-50<c.ycor()<b.ycor()+50) :
		c.setx(340)
		dx*=-1
	if (-350<c.xcor()<-340) and (a.ycor()-50<c.ycor()<a.ycor()+50):
		c.setx(-340)
		dx*=-1



