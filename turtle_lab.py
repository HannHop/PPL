import turtle
# turtle part
tur = turtle.Turtle()
tur.speed('fastest')


def fractal_square(x):
 if x<=1:
  return
 tur.forward(x) # go x
 tur.left(90) # turn right by 90 deg angle
 tur.forward(x) # go x right
 tur.left(90) # turn d
 tur.forward(x) # go x down
 tur.left(90) # turn left
 tur.forward(x) # go to the beginning pointp
 tur.left(90)
 #tur.right(90)
 fractal_square(0.9 * x)
 
fractal_square(200)
