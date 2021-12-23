import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
carmanager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(fun= player.move, key= "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    carmanager.create_car()
    carmanager.move()

    #Detect collision of turtle and car
    
    for car in carmanager.allcars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when player reaches end line
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.level_up()
        

screen.exitonclick()