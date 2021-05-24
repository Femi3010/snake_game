from turtle import Turtle,Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.title("Snake game")
screen.bgcolor("black")
screen.tracer(0)
snake=Snake()
food=Food()
score_board=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_starts=True
while game_starts:
    screen.update()
    time.sleep(.15)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        game_starts=False
        score_board.game_over()
    for segment in snake.segments[1:]:

        if snake.segments[0].distance(segment)<10:
            game_starts = False
            score_board.game_over()




screen.exitonclick()