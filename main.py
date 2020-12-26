from score_board import Scoreboard
from turtle import *

from space_ship import Spaceship
from asteroid import Asteroid
from time import sleep

# Screen Setup
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor('Black')
screen.title('Asteroids')
screen.tracer(0)


#Instantiant the Spaceship
spaceship = Spaceship()

#Instantiant the Asteroid
asteroid = Asteroid()

#Instantiant the Scoreboard
scoreboard = Scoreboard()


#Move the Spaceship across the Screen
screen.listen()
screen.onkey(spaceship.up,"Up")
screen.onkey(spaceship.down, "Down")
screen.onkey(spaceship.left,"Left")
screen.onkey(spaceship.right, "Right")


#Game Logic
game_is_on = True

while game_is_on:
    sleep(.01)
    screen.update()
    asteroid.move_asteroid()

    # Detect Asteroid Collision with top and bottom walls
    if asteroid.ycor() > 280 or asteroid.ycor() < -280:
        asteroid.bounce_y()

    #Detect Asteroid Collision with side walls
    if asteroid.xcor() > 380 or asteroid.xcor() < -380:
        asteroid.bounce_x()

    #Detect Collision with Spaceship and Asteroid
    if spaceship.distance(asteroid) < 40:
        print("COLLISION")
        game_is_on = False


screen.exitonclick()