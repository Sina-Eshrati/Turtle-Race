from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=800, height=600)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

play_again = "yes"

while play_again == 'yes':
    screen.clear()
    user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")
    is_race_on = False
    while user_bet not in colors:
        user_bet = screen.textinput(title="oops! Wrong color", prompt="Choose a color in rainbow: ")
    else:
        is_race_on = True

    starting_point_y = -210
    turtles = []
    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.speed(10)
        new_turtle.goto(-380, starting_point_y)
        turtles.append(new_turtle)
        starting_point_y += 75

    while is_race_on:
        for turtle in turtles:
            turtle.forward(randint(0, 10))
            if turtle.xcor() > 360:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    play_again = screen.textinput(title="replay", prompt=f"Congratulations! {winning_color} turtle won the race. Do you want to play again? ").lower()
                else:
                    play_again = screen.textinput(title="replay", prompt=f"Sorry you lost! {winning_color} turtle won the race. Do you want to play again? ").lower()


screen.exitonclick()
