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

BULLET_SPEED = 10

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


bullet_is_ready = True
direction = spaceship.heading()
def setup_bullet():
    #Move the bullet to be just above the player
    x = spaceship.xcor()
    y = spaceship.ycor()
    bullet.setheading(spaceship.heading())
    bullet.setposition(x,y)

def fire_bullet():
    #declare bullet_is_ready and direaction  as a global incase it needs changing
    global direction, bullet_is_ready      
    if bullet_is_ready:
        bullet_is_ready = False
        direction = spaceship.heading()
        #Move the bullet to be just above the player
        setup_bullet()
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
score = 0
add_one_available = True


setup_bullet()

while game_is_on:

    sleep(.01)
    screen.update()
    #Move the Asteroid  
    asteroid.move_asteroids()
    
    if bullet_is_ready:
        setup_bullet()

    if score > 2 and score % 3 == 0 and add_one_available:
        for _ in range(3):
            asteroid.add_one_asteroid()
        add_one_available = False
    elif score % 3 != 0:
        add_one_available = True


    
    #Move the Bullet
    if not bullet_is_ready:
        if direction == UP:
            y = bullet.ycor()
            y += BULLET_SPEED
            bullet.sety(y)
            
        
        if direction == DOWN:
            y = bullet.ycor()
            y -= BULLET_SPEED
            bullet.sety(y)
        
        if direction == LEFT:
            x = bullet.xcor()
            x -= BULLET_SPEED
            bullet.setx(x)
        
        if direction == RIGHT:
            x = bullet.xcor()
            x += BULLET_SPEED
            bullet.setx(x)

    # Check to see if the bullet has reached the top or bottom
    if bullet.ycor() > 280 or bullet.ycor() < -280:
        bullet.hideturtle()
        bullet_is_ready = True
    
    # Check to see if the bullet has reached the left or right
    if bullet.xcor() > 380 or bullet.xcor() < -380:
        bullet.hideturtle()
        bullet_is_ready = True  
    
    


 

    # Detect Asteroid Collision with top and bottom walls
    asteroid.bounce_y()

    # Detect Asteroid Collision with left and  walls
    asteroid.bounce_x()

    #Detect if collision and makes asteroids bounce against themselves
    


    for a in asteroid.asteroids:        
        # Detect Collision with Spaceship and Asteroid
        if spaceship.distance(a) < 35:
            print("COLLISION")
            scoreboard.reset()
            
            # game_is_on = False
        # Detect Collision with Bullet and Asteroid
        if bullet.distance(a) < 30 and bullet.distance(spaceship) > 5:
            setup_bullet()
            bullet.hideturtle()
                    
            bullet_is_ready = True 
            a.goto(-10000,0)            
            scoreboard.add_one_to_score()
            score += 1
            print("COLLISION WITH BULLET score: ", score)
    


        
        


   

    
    


screen.exitonclick()