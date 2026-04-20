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

circle()

window.exitonclick()