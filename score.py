from turtle import *
import random
import turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        with open('snakegame/high_score.txt', 'r') as f:
            self.high_score = int(f.read())
            f.close()

            
        self.hideturtle()
        self.penup()
        
        self.goto(0, 260)
        self.color("white")
        self.write(f"Score: {self.score} | High score: {self.high_score}", align="center")
        



    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.color("#EE4B2B")
        self.write(f"GAME OVER (Score: {self.score})", align="center", font=('Arial', 30, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snakegame/high_score.txt', 'w') as f:
                new_highscore = str(self.high_score)
                f.write(new_highscore)
                f.close()

        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | High score: {self.high_score}", align="center")

    def end(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('snakegame/high_score.txt', 'w') as f:
                new_highscore = str(self.high_score)
                f.write(new_highscore)
                f.close()
        turtle.bye()