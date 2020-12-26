from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = 'left'
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle
        self.goto(-370, 250)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align = ALIGNMENT, font = FONT)