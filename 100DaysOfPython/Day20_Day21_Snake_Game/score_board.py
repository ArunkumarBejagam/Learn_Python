from turtle import Turtle
FONT = ('Calibri', 20, 'bold')
ALIGNMENT = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.setpos(x=0, y=270)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score Board : {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def collision(self):
        self.setpos(x=0, y=0)
        self.write("GAME OVER! ", align=ALIGNMENT, font=FONT)
