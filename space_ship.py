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
        self.setheading(UP)
        self.forward(20)
        if self.ycor() > 300:
            self.goto(self.xcor(), -300)
            

    def down(self):
        self.setheading(DOWN)
        self.forward(20)
        if self.ycor() < -300:
            self.goto(self.xcor(), 300)            
        

    def left(self):
        self.setheading(LEFT)
        self.forward(20)
        if self.xcor() < -380:
            self.goto(380, self.ycor())            
        

    def right(self):
        self.setheading(RIGHT)
        self.forward(20)
        if self.xcor() > 380:
            self.goto(-380, self.ycor())

    
        
