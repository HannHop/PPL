import turtle

tur = turtle.Turtle()
tur.speed('fast')

class Tree:
 def __init__(self, s, l, a):
  self.s=s
  self.l=l
  self.a=a

 @staticmethod
 def fractal_tree(s, l, a):
  if l==0:
   return
  tur.forward(s)
  tur.right(a)
  Tree.fractal_tree(s*0.9, l-1, a)
  tur.left(a*2)
  Tree.fractal_tree(s*0.9, l-1, a)
  tur.right(a)
  tur.backward(s)

tree1=Tree(70, 6, 30) 
tree1.fractal_tree(70, 6, 30)