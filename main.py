import time
from turtle import Turtle, Screen
from player import Player
from car_manager import Car_Manager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game = True

while game:
    time.sleep(0.1)
    screen.update()