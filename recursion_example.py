import turtle


def draw_triangle(vertices, depth):
    if depth == 0:
        turtle.up()
        turtle.goto(vertices[0][0], vertices[0][1])
        turtle.down()
        for vertex in vertices:
            turtle.goto(vertex[0], vertex[1])
        turtle.goto(vertices[0][0], vertices[0][1])
    else:
        midpoints = [
            (
                (vertices[0][0] + vertices[1][0]) / 2,
                (vertices[0][1] + vertices[1][1]) / 2,
            ),
            (
                (vertices[1][0] + vertices[2][0]) / 2,
                (vertices[1][1] + vertices[2][1]) / 2,
            ),
            (
                (vertices[2][0] + vertices[0][0]) / 2,
                (vertices[2][1] + vertices[0][1]) / 2,
            ),
        ]

        draw_triangle([vertices[0], midpoints[0], midpoints[2]], depth - 1)
        draw_triangle([midpoints[0], vertices[1], midpoints[1]], depth - 1)
        draw_triangle([midpoints[2], midpoints[1], vertices[2]], depth - 1)


def main():
    turtle.speed(2)
    turtle.color("blue")

    vertices = [(-200, -100), (0, 200), (200, -100)]
    depth = 5

    draw_triangle(vertices, depth)

    turtle.hideturtle()
    turtle.done()


if __name__ == "__main__":
    main()
