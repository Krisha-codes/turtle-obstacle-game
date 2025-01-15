FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-230,250)

    def display(self,score):
        self.clear()
        self.write(f"Level {score}", align="center", font= FONT)


