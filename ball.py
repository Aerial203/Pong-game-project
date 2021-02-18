from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pos = 10
        self.y_pos = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_pos
        new_y = self.ycor() + self.y_pos
        # print(f"{new_x}, {new_y}")
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_pos *= -1
        # print(self.y_pos)

    def bounce_x(self):
        self.x_pos *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
