from turtle import Turtle

from random import randint

STARTING_MOVE_DISTANCE = 5
NUMBER_OF_ASTEROIDS = 1
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class AsteroidManager:
    def __init__(self):
        self.all_asteroids = []
        self.asteroid_speed = STARTING_MOVE_DISTANCE
        
    def create_asteroid(self):
        for _ in range(NUMBER_OF_ASTEROIDS):
            new_asteroid = Turtle('circle')
            new_asteroid.shapesize(4,4)
            new_asteroid.color('white')
            new_asteroid.shape('circle')        
            new_asteroid.setheading(RIGHT)
            new_asteroid.penup()
            new_asteroid.shapesize(4,4)
            self.all_asteroids.append(new_asteroid)
        print(self.all_asteroids)

    def move_asteroid(self):
        for asteroid in self.all_asteroids:
            print(asteroid)

