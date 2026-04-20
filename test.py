from turtle import Turtle, Screen
le = Turtle()
window = Screen()
window.setup(800, 800)
window.bgcolor('black')

le.shape('turtle')
le.color('orange')
le.pensize(2)
le.speed('fastest')
def circle():
   le.penup()
   le.goto(-200, -200)
   le.pendown()
   for _ in range(20):
      le.circle(50)
      le.left(360 / 20)

def sqeare():
   le.penup()
   le.goto(0, 0)
   le.pendown()
   for _ in range(10):
      for _ in range(4):
         le.forward(50)
         le.left(90)
        
      le.left(360 / 10)



circle()
sqeare()

window.exitonclick()