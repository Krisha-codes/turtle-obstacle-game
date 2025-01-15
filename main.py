import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
manage_car = CarManager()
score = Scoreboard()
player = Player()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
game_is_on = True
score_player = 1
score.display(score_player)
while game_is_on:
    time.sleep(0.1)
    screen.update()

    screen.onkey(player.go_up, "Up")
    if player.ycor()>280:
        score_player +=1
        score.display(score_player)
        player.restart()

        manage_car.level_up()
    manage_car.create_cars()
    manage_car.move_cars()
    for car in manage_car.all_cars:
        if car.distance(player)<20:
            game_is_on = False
            turtle = Turtle()
            turtle.penup()
            turtle.write("GAME OVER", align="center", font=("Courier", 80, "normal"))


screen.exitonclick()