from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

"""Turtle moves up with up key"""
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.restart()
    def restart(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
    def go_up(self):
        self.forward(MOVE_DISTANCE)






