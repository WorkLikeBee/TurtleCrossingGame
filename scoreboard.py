from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.write(arg=f"Level: {self.level}", align="center",font=FONT)

    def update_scoreboard(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center",font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="Game over",align="center",font=FONT)