import turtle
# turtle part
tur = turtle.Turtle()
tur.speed('fastest')

# the turtle will go in anti-clockwise direction starting from its default beginning
def fractal_square(x):
 if x<=1:
  return
 tur.forward(x) # go x
 tur.left(90) # turn by 90 deg angle
 tur.forward(x) # go x left
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
 tur.forward(x) 
 tur.left(120)
 tur.forward(x) 
 tur.left(120) 
 tur.forward(x)
 tur.left(120)
 fractal_triangle(0.9 * x)

fractal_triangle(300)
