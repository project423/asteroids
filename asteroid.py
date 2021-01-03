from asteroid_manager import NUMBER_OF_ASTEROIDS
from turtle import Turtle

from random import randint


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_ASTEROIDS = 5

class Asteroid(Turtle):
    def __init__(self):
        super().__init__()
        self.asteroids = []
        self.asteroid_speed = STARTING_MOVE_DISTANCE
        self.create_asteroids()
        self.hideturtle()
        

    def create_asteroids(self):
        for _ in range(NUMBER_OF_ASTEROIDS):  
            self.add_one_asteroid()      
    


    def move_asteroids(self):
        for asteroid in self.asteroids:
            new_y = asteroid.ycor() + asteroid.dy
            new_x = asteroid.xcor() + asteroid.dx
            asteroid.goto(new_x,new_y)
    
            
    def add_one_asteroid(self):
        new_asteroid = Turtle('circle')
        new_asteroid.shapesize(4,4)
        new_asteroid.penup()
        new_asteroid.color('white')
        new_asteroid.dy = 3
        new_asteroid.dx = 3
        # Logic so the asteroids won't spawn on top of the ship
        random_y_top = randint(100, 280)
        random_y_bottom = randint(-280, -100)
        random_x_left = randint(-380, -100)
        random_x_right = randint(100, 380)
        random_x = [random_x_left, random_x_right][randint(0,1)]
        random_y = [random_y_top, random_y_bottom][randint(0,1)]
        
        new_asteroid.goto(random_x,random_y)
        self.asteroids.append(new_asteroid)

    
    

    def bounce_y(self):
        for asteroid in self.asteroids:
            if asteroid.ycor() > 280 or asteroid.ycor() < -280:
                asteroid.dy *= - 1

    def bounce_x(self):
        for asteroid in self.asteroids:
            if asteroid.xcor() > 380 or asteroid.xcor() < -380:
                asteroid.dx *= -1

    def get_list_of_asteroids(self):
        return self.asteroids

    def asteroids_collision(self):
        for index, this in enumerate(self.asteroids):
            for that in self.asteroids[index+1:]:
                print(this, that)


    


    

    