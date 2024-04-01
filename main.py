from snake import Snake, screen
from food import Food
from score import Score

is_game_on = True

snake = Snake()
score = Score()
snake.create_snake()

def end_game():
    print("Called")


screen.listen()
screen.onkey(snake.dir_right, "Right")
screen.onkey(snake.dir_left, "Left")
screen.onkey(snake.dir_up, "Up") 
screen.onkey(snake.dir_down, "Down")
screen.onkeypress(score.end, "a")



food=Food()
food.reposition()

while is_game_on:
    snake.move_forward()

    if snake.segments[0].distance(food) < 20:
        food.reposition()
        score.increase_score()
        snake.extend()

    elif snake.segments[0].xcor() == -280 or snake.segments[0].xcor() == 280:
        score.reset()
        snake.reset()


    elif snake.segments[0].ycor() == -280 or snake.segments[0].ycor() == 280:
        score.reset()
        snake.reset()


    for segment in snake.segments:
        
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            score.reset()
            snake.reset()

