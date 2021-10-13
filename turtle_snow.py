import turtle

tur = turtle.Turtle()
tur.speed('fastest')

class Snowflake:
 def __init__(self, len, lev):
  self.len=len
  self.lev=lev

 @staticmethod
 def snowy(len, lev):
  if lev==0:
   tur.forward(len)
   return
  len/=3.0
  Snowflake.snowy(len, lev-1)
  tur.left(60)
  Snowflake.snowy(len,lev-1)
  tur.right(120)
  Snowflake.snowy(len,lev-1)
  tur.left(60)
  Snowflake.snowy(len,lev-1)

 @staticmethod
 def draw():
  for i in range(3):
   snowy(len, 5)
   right(120)

snow=Snowflake(300,5)
Snowflake.snowy(snow.len, snow.lev)

  