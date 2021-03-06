from turtle import Turtle, heading

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed_x = 5
        self.speed_y = 5
        self.goto(0,0)



    def move(self):
        self.goto(self.xcor() + self.speed_x, self.ycor() + self.speed_y )
       
    def bounce_y(self):
        self.speed_y *= -1

    def bounce_x(self):
        self.speed_x *= -1

    def refresh(self):
        self.goto(0,0)
        self.speed_x *= -1
       
        