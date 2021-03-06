from score_board import ScoreBoard
from turtle import Screen, distance
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.listen()

score_board = ScoreBoard()

is_game_on = True

r_paddle = Paddle((350,20),'blue')
l_paddle = Paddle((-350,20),'red')

ball = Ball()

screen.bgcolor('black')




screen.onkeypress(fun=r_paddle.move_up, key='Up')
screen.onkeypress(fun=r_paddle.move_down, key='Down')

screen.onkeypress(fun=l_paddle.move_up, key='w')
screen.onkeypress(fun=l_paddle.move_down, key='s')
screen.onkeypress(fun=screen.bye, key='q')



while is_game_on:
    screen.update()
    time.sleep(0.01)
    ball.move()

    #Collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()


    #Collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
       ball.bounce_x()
    

    
    if ball.xcor() > 405 : 
       ball.refresh()
       score_board.l_score += 1
       score_board.refresh()

    if ball.xcor() < -405:
        ball.refresh()
        score_board.r_score += 1
        score_board.refresh()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    

    

        
    






screen.exitonclick()