from turtle import Turtle
import turtle

FONT = ("Courier",80,'normal')

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.refresh()


    def refresh(self):
        self.reset()
        self.penup()
        self.goto(-100,200)
        self.color('red')
        self.hideturtle()
        self.write(arg=f"{self.l_score} " ,move=False , font=FONT)
        self.color('white')
        self.goto(0,200)
        self.write(arg='/',move=False , font=FONT)
        self.goto(100,200)
        self.color('blue')
        self.write(arg=f"{self.r_score}" ,move=False , font=FONT)