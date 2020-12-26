from turtle import *

from score_board import Scoreboard
from space_ship import Spaceship
from asteroid import Asteroid
from bullet import Bullet
from time import sleep

UP = 90.00
DOWN = 270.0
LEFT = 180.0
RIGHT = 0.0

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


    
#Create the player's bullet

bullet = Bullet()
# bullet.color("white")
# bullet.shape("triangle")
# bullet.penup()
# bullet.speed(0)
# bullet.setheading(90)
# bullet.shapesize(0.5, 0.5)
# bullet.hideturtle()

bulletspeed = 2


#Dfine bullet state
# read - ready to fire

#fire - bullet is firing
bulletstate = "ready"

def fire_bullet():
    #declare bulletstate as a global if it needs changing
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to be just above the player
        x = spaceship.xcor()
        y = spaceship.ycor()
        print(bullet.xcor(),bullet.ycor())
        bullet.setheading(spaceship.heading())
        bullet.setposition(x,y)
        bullet.showturtle()



    

#Create the keyboard bindings
screen.listen()
screen.onkey(spaceship.up,"Up")
screen.onkey(spaceship.down, "Down")
screen.onkey(spaceship.left,"Left")
screen.onkey(spaceship.right, "Right")
screen.onkey(fire_bullet, 'space')







#Game Logic
game_is_on = True

while game_is_on:
    sleep(.01)
    screen.update()
    #Move the Asteroid
    asteroid.move_asteroid()

    #Move the Bullet
    if bulletstate == "fire":
        if spaceship.heading() == UP:
            y = bullet.ycor()
            y +=bulletspeed
            bullet.sety(y)
        elif spaceship.heading() == DOWN:
            y = bullet.ycor()
            y -=bulletspeed
            bullet.sety(y)
        elif spaceship.heading() == LEFT:
            x = bullet.xcor()
            x -=bulletspeed
            bullet.setx(x)
        elif spaceship.heading() == RIGHT:
            x = bullet.xcor()
            x +=bulletspeed
            bullet.setx(x)

    # Check to see if the bullet has reached the top 
    if bullet.ycor() > 280 or bullet.ycor() < -280:
        bullet.hideturtle()
        bulletstate = "ready"
    
    if bullet.xcor() > 380 or bullet.xcor() < -380:
        bullet.hideturtle()
        bulletstate = "ready"  
    
    

    

    # Detect Asteroid Collision with top and bottom walls
    if asteroid.ycor() > 280 or asteroid.ycor() < -280:
        asteroid.bounce_y()

    #Detect Asteroid Collision with side walls
    if asteroid.xcor() > 380 or asteroid.xcor() < -380:
        asteroid.bounce_x()

    #Detect Collision with Spaceship and Asteroid
    # if spaceship.distance(asteroid) < 40:
    #     print("COLLISION")
    #     game_is_on = False


   

    
    


screen.exitonclick()