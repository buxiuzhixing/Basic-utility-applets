import random as r
import turtle as t
import time as i
t.width(10)
t.speed(30)
w=0
a=int(input("请输入指定学号："))
while True:
  w=w+1
  m=r.randint(1,41)
  print(m)
  t.clear()
  t.penup()
  t.goto(-150,-150)
  t.pendown()
  t.write(m,font=("Arial",250))
  i.sleep(0.1)
  if m==a:
    t.penup()
    t.goto(0,-200)
    t.pendown()
    t.circle(250)
    print("抽了",w,"次")
    t.bgcolor("green")
    a=input("OK")
    break
