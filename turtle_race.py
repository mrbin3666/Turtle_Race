from turtle import *
from random import *
import random
import os
#how to add background color
import turtle
import pygame

#background

win=turtle.Screen()
win.setup(width=960, height=540)
bgpic = "beach.gif"
win.addshape(bgpic)
sh=turtle.Turtle()
sh.shape(bgpic)

#sound
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('nhac.mp3')
pygame.mixer.music.play()


#Number of player
number=int(input("nhap so rua(1-5): "))

#Creating the finish line.
finish = turtle.Turtle()
finish.up	()	#Allowing to move the finish line to a certain location.
finish.speed(0)
finish.goto(160,30) #Moving the finish line to the correct position.
finish.down()
finish.right(90)
finish.width(5)


#Drawing the finish line.
for i in range(17):
	finish.color("blue")
	finish.forward(5)
	finish.color("red")
	finish.forward(5)


#Creating the text to say "Finish line"
finish_text = turtle.Turtle()
finish_text.up()
finish_text.speed(10)
finish_text.color("White")
finish_text.goto(110, 40)
finish_text.write("Finish Line", font = ("Times New Roman",12, "bold"))


#Creating another turtle for the starting line.
start = turtle.Turtle()
start.up()
start.speed(0)
start.goto(-140, 30)
start.width(5)
start.right(90)
start.down()

#Drawing the starting line.
for i in range(17):
	start.color("green")
	start.forward(5)
	start.color("yellow")
	start.forward(5)

#Creating the text to say "Finish line"
start_text = turtle.Turtle()
start_text.up()
start_text.speed(10)
start_text.color("white")
start_text.goto(-160, 40)
start_text.write("Starting Line", font = ("Times New Roman",12, "bold"))

#print the track markers
speed(10)
penup()
goto(-120,40)

for step in range(14):
  right(90)
  for num in range(8):
    penup()
    forward(10)
    pendown()
    color("white")
    forward(10)
  penup()
  backward(160)
  left(90)
  forward(20)

#This is actually moving the text to its correct location and writing it so that people can see it.
first_text = turtle.Turtle()
first_text.speed(10)
first_text.up()
first_text.color("yellow")
first_text.goto(-180, -140)
first_text.write("GET TO YOUR STARTING POSITIONS!!!!!", font = ("Times New Roman", 14, "normal"))
first_text.down()
  
#Creating the turtles for the race and their colours.
_turtle=['1','2','3','4','5']
colour=['red','blue','green','yellow','black']
turtleRow=[]
for i in range(number):
	_turtle[i] = Turtle()
	_turtle[i].color(colour[i])
	_turtle[i].shape('turtle')

	_turtle[i].penup()
	_turtle[i].goto(-160,-90+(120/number)*i)
	turtleRow.append(-90+(120/number)*i)

	for turn in range(4):
	  _turtle[i].left(90)

#Removing the old text and creating space for the new text.
first_text.clear()

#Racelight Countdown 
#Creating the first red circle as a turtle.
red_circle_1 = turtle.Turtle()
red_circle_1.speed(1)
red_circle_1.up()
red_circle_1.goto(0, 30)
red_circle_1.color("red")
red_circle_1.shape("circle")


#Creating the second red circle indicating starting is about to begin.
red_circle_2 = turtle.Turtle()
red_circle_2.speed(1)
red_circle_2.up()
red_circle_2.goto(0, 0)
red_circle_2.color("red")
red_circle_2.shape("circle")

#Creating the third red circle indicating starting is about to begin.
red_circle_3 = turtle.Turtle()
red_circle_3.speed(1)
red_circle_3.up()
red_circle_3.goto(0, -30)
red_circle_3.color("red")
red_circle_3.shape("circle")

#Creating the first green circle indicating starting is about to begin.
green_circle_1 = turtle.Turtle()
green_circle_1.speed(1)
green_circle_1.up()
green_circle_1.goto(0, -60)
green_circle_1.color("green")
green_circle_1.shape("circle")
green_circle_1.pensize(100)

red_circle_1.ht()
red_circle_2.ht()
red_circle_3.ht()
green_circle_1.ht()

##Buff

buff_y=random.choice(turtleRow)
buff = turtle.Turtle()
buff.width(5)
buff.speed(1)
buff.up()
buff.goto(-90, buff_y)
buff.color("red")
buff.shape("circle")
buff.shapesize(0.5)

#Debuff

debuff_y=random.choice(turtleRow)
while(debuff_y==buff_y):
	debuff_y=random.choice(turtleRow)
debuff = turtle.Turtle()
debuff.width(5)
debuff.speed(1)
debuff.up()
debuff.goto(-20, debuff_y)
debuff.color("green")
debuff.shape("circle")
debuff.shapesize(0.5)

##the actual race!
turtleFinished=0
backwardStep=0
eatDebuff=False
while 1:
	if turtleFinished==number: break
	for i in range(number):
		if _turtle[i].ycor() > -100:
			if(_turtle[i].position()>=buff.position() and buff_y==turtleRow[i]):
				_turtle[i].forward(randint(3,6))
				buff.ht()
			elif(_turtle[i].position()>=debuff.position() and debuff_y==turtleRow[i]):
				eatDebuff=True
				_turtle[i].left(180)
				_turtle[i].setheading(180)
				debuff.ht()
				debuff.goto(170, debuff_y)

			else:
				if(backwardStep>40 and debuff_y==turtleRow[i]):
					_turtle[i].setheading(360)

					backwardStep=0
					eatDebuff=False
				else:
					_turtle[i].forward(randint(1,5))


				if(eatDebuff):
					backwardStep+=1





			if _turtle[i].xcor() >= 160:
				turtleFinished+=1
				_turtle[i].goto(-80, -100-30*turtleFinished)
				_turtle[i].write("Rank: "+str(turtleFinished), font = ("Times New Roman", 14, "normal"))
				_turtle[i].left(360)




	
