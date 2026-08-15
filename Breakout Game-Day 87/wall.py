from turtle import Turtle

COLORS = ["red", "blue", "green"]
POINTS = [3, 2, 1]


class Wall:
    def __init__(self):
        starting_x = -280
        starting_y = 250
        spacing = 60          # horizontal distance between brick centers
        row_height = 30        # vertical distance between rows

        self.bricks = []

        for i in range(6):                 # 6 rows total
            color = COLORS[i // 2]          # 0,1 -> COLORS[0]; 2,3 -> COLORS[1]; 4,5 -> COLORS[2]
            points = POINTS[i // 2]

            bricks = []
            y = starting_y - (i * row_height)

            for j in range(10):             # 10 bricks per row
                x = starting_x + (j * spacing)

                brick = Turtle()
                brick.shape("square")
                brick.color(color)
                brick.shapesize(stretch_wid=1, stretch_len=2)
                brick.penup()
                brick.goto(x, y)

                bricks.append(brick)

            brick_row = {
                'color': color,
                'points': points,
                'bricks': bricks
            }
            self.bricks.append(brick_row)