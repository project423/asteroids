from turtle import Turtle

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        # self.bullet = Turtle()
        self.hideturtle()
        self.color('white')
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.shapesize(0.5, 0.5)


    


    
