COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance== 1:
            new_car = Turtle("square")
            new_car.penup()
            x = random.randint(0, 5)
            new_car.color(COLORS[x])
            new_car.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            new_ycor= random.randint(-250,250)
            new_car.goto(280,new_ycor)
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.carspeed)
    def level_up(self):
        self.carspeed += MOVE_INCREMENT







