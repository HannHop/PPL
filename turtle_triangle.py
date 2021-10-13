import turtle
# turtle part
t = turtle.Turtle()
t.speed('fastest')

def S_triangle(a):
    if a>=5:
        for i in range(3):
            S_triangle(a/2)
            t.forward(a)
            t.left(120)
    else:
        return
S_triangle(200)
