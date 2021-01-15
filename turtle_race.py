from turtle import Screen, Turtle
import random


screen = Screen()
screen.setup(width = 600, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter your choice: ")

colors = ["red", "blue", "green", "yellow", "orange", "purple"]
y_positions = [-100, -50, 0, 50 , 100, 150]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):

	new_turtle = Turtle(shape = "turtle")
	new_turtle.penup()
	new_turtle.color(colors[turtle_index])
	new_turtle.goto(x = -270, y = y_positions[turtle_index])
	all_turtles.append(new_turtle)

if user_bet:
	is_race_on = True

while is_race_on:
	for turtle in all_turtles:
		if turtle.xcor() >270:
			winnig_turtle = turtle.pencolor()
			is_race_on = False
			if winnig_turtle == user_bet:
				print(f'Your {user_bet} turtle has won the race')
				
			else:
				print(f'Sorry {winnig_turtle} turtle has won the race')
		
		rand_distance = random.randint(0, 10)
		turtle.forward(rand_distance)



























screen.exitonclick()