import turtle
# turtle part
tur = turtle.Turtle()
tur.speed('fastest')


def fractal_square(x):
 if x<=1:
  return
 tur.forward(x) # go x
 tur.left(90) # turn by 90 deg angle
 tur.forward(x) # go x right
 tur.left(90) # turn d
 tur.forward(x) # go x down
 tur.left(90) # turn left
 tur.forward(x) # go to the beginning point
 tur.left(90)
 fractal_square(0.9 * x)
 
fractal_square(200)

def fractal_triangle(x):
 if x<=1:
  return
 tur.forward(x) # go x
 tur.left(120)
 tur.forward(x) # go x right
 tur.left(120) # turn d
 tur.forward(x) # go x down
 tur.left(120) # turn left
 #tur.forward(x) # go to the beginning pointp
 #tur.left(120)
 #tur.right(90)
 fractal_triangle(0.9 * x)

fractal_triangle(300)