import random as r
import turtle as t
import time
m=r.randint(1,41)
t.speed(30)
t.width(10)
for i in range(3):
  t.clear()
  d=r.randint(1,41)
  t.penup()
  t.goto(-150,-150)
  t.pendown()
  t.write(d,font=("Arial",250))
  time.sleep(0.1)
while True:
  print(m)
  t.clear()
  t.bgcolor("green")
  t.penup()
  t.goto(-150,-150)
  t.pendown()
  t.write(m,font=("Arial",250))
  t.penup()
  t.goto(0,-200)
  t.pendown()
  t.circle(250)
  a=input("回车以继续")
  m=r.randint(1,41)
  print(m)
