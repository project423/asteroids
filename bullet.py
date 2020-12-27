from turtle import Turtle


# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0


# class Bullet(Turtle):
#     def __init__(self, x, y, direction):
#         super().__init__()
#         self.x = x
#         self.y = y
#         self.y_move = 3
#         self.x_move = 3
#         self.direction = direction
#         self.hideturtle()
#         self.color('white')
#         self.penup()
#         self.shape('triangle')
#         self.speed(0)
#         self.shapesize(0.5,0.5)
#         self.setheading(direction)
#         self.hideturtle()
#         self.bullet_speed = 20
#         self.bullet_state = "ready"
#         self.spawn_bullet()
        

#     def spawn_bullet(self):
#         self.showturtle()
#         self.setheading(self.direction)
#         if self.direction == UP:
#             self.goto(self.x, self.y + 10)
#         elif self.direction == DOWN:
#             self.goto(self.x, self.y - 10)
#         elif self.direction == LEFT:
#             self.goto(self.x - 10, self.y)
#         elif self.direction == RIGHT:
#             self.goto(self.x + 10, self.y)
#         self.bullet_is_live = True
        

#     def fire_bullet(self):
#         self.bullet_state = 

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


    


    
