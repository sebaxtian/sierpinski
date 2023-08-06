import turtle


def get_points(surface=(1024, 1024)):
    x_axis = (surface[0] / 2) - 20
    y_axis = (surface[1] / 2) - 20

    point1 = (0, y_axis)
    point2 = (-x_axis, -y_axis)
    point3 = (x_axis, -y_axis)

    return point1, point2, point3


def draw_line(point1, point2, pen=None):
    pen.goto(point1[0], point1[1])
    pen.down()
    pen.goto(point2[0], point2[1])
    pen.up()


def midpoint(point1, point2):
    x = (point1[0] + point2[0]) / 2
    y = (point1[1] + point2[1]) / 2

    return x, y


def draw_point(x, y, pen=None):
    pen.goto(x, y)
    pen.down()
    pen.dot(5, "black")
    pen.up()


def step0(point1, point2, point3, pen=None):
    # Lines
    # pen.begin_fill()
    draw_line(point1, point2, pen)
    draw_line(point2, point3, pen)
    draw_line(point3, point1, pen)
    # pen.end_fill()
    # Middle Points
    x, y = midpoint(point1, point2)
    draw_point(x, y, pen)
    x, y = midpoint(point2, point3)
    draw_point(x, y, pen)
    x, y = midpoint(point3, point1)
    draw_point(x, y, pen)


def sierpinski(point1, point2, point3, level=1, pen=None):
    # colors = ['blue','red','green','yellow','violet','orange']
    # pen.fillcolor(colors[level])
    step0(point1, point2, point3, pen)
    if level > 0:
        sierpinski(
            point1, midpoint(point1, point2), midpoint(point3, point1), level - 1, pen
        )
        sierpinski(
            point2, midpoint(point1, point2), midpoint(point2, point3), level - 1, pen
        )
        sierpinski(
            point3, midpoint(point2, point3), midpoint(point3, point1), level - 1, pen
        )


def main():
    print("Sierpinski Triangle")

    screen = turtle.Screen()
    screen.title("Sierpinski Triangle")
    screen.setup(width=1024, height=1024)
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.hideturtle()
    # pen.speed(3)
    pen.speed(0)
    pen.color("white")
    pen.up()

    point1, point2, point3 = get_points()
    sierpinski(point1, point2, point3, 5, pen)

    screen.exitonclick()


if __name__ == "__main__":
    main()
