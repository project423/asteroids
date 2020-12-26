from turtle import Turtle

from random import randint


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Asteroid(Turtle):
    def __init__(self):
        super().__init__()
        self.y_move = 3
        self.x_move = 3
        self.color('white')
        self.shape('circle')        
        self.setheading(RIGHT)
        self.penup()
        self.shapesize(4,4)
        self.spawn_asteroid()

    def spawn_asteroid(self):
        random_x = randint(-280,280)
        random_y = randint(-280,280)
        self.goto(random_x,random_y)
        
    def move_asteroid(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x,new_y)
    
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1