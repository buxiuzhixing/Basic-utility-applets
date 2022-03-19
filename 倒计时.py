import time
import turtle as t
w=int(input("输入倒计时长，以秒为单位："))
t.width(10)
t.speed(30)
while True:
    w=w-1
    print(w)
    t.clear()
    t.penup()
    t.goto(-150,-150)
    t.pendown()
    t.write(w,font=("Arial",250))
    time.sleep(1)
    if w==0:
        print("时间到！")
        t.penup()
        t.goto(0,-200)
        t.pendown()
        t.circle(250)
        t.bgcolor("green")
        o=input("ok")
        break
