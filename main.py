rate=6
usd=100
cny=usd*rate
print(f"{usd}美元={cny}人民币")
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
for i in range(4):
    turtle.pencolor(colors[i % len(colors)])
    turtle.seth(-40)
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.pencolor(colors[4 % len(colors)])
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.pencolor(colors[5 % len(colors)])
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()
import turtle
turtle.seth(0)
turtle.fd(100)
turtle.seth(120)
turtle.fd(100)
turtle.seth(240)
turtle.fd(100)
import turtle
turtle.speed(0)
length=5
for i in range(100):
    turtle.fd(length)
    turtle.right(90)
    length+=5
turtle.done()
 
