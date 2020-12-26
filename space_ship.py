from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Spaceship(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.setheading(90)
        self.shapesize(2,2)

    def up(self):
        if self.ycor() < 300:
            self.setheading(UP)
            self.forward(20)
            

    def down(self):
        if self.ycor() > -300:
            self.setheading(DOWN)
            self.forward(20)
            
        

    def left(self):
        if self.xcor() > -380:
            self.setheading(LEFT)
            self.forward(20)
            
        

    def right(self):        
        if self.xcor() < 380:
            self.setheading(RIGHT)
            self.forward(20)
        
