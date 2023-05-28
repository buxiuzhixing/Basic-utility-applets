import tkinter as tk
import time as t

# 设置窗口大小和标题
WIDTH = 500
HEIGHT = 500
TITLE = "Bouncing Balls"
root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")
root.title(TITLE)

# 创建画布
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# 创建小球对象
class Ball:
    def __init__(self, x, y, radius, color, x_speed, y_speed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.shape = canvas.create_oval(self.x - self.radius, self.y - self.radius, 
                                         self.x + self.radius, self.y + self.radius, 
                                         fill=self.color)
        
    def move(self):
        # 移动小球
        self.x += self.x_speed
        self.y += self.y_speed
        
        # 检查小球是否碰到窗口边缘
        if self.x - self.radius < 0 or self.x + self.radius > WIDTH:
            self.x_speed = -self.x_speed
        if self.y - self.radius < 0 or self.y + self.radius > HEIGHT:
            self.y_speed = -self.y_speed
        
        # 更新小球的位置
        canvas.move(self.shape, self.x_speed, self.y_speed)
    
# 创建两个小球并启动动画
ball1 = Ball(100, 100, 30, "blue", 5, 10)
ball2 = Ball(200, 150, 20, "red", 8, 6)

while True:
    ball1.move()
    ball2.move()
    root.update()
    t.sleep(50)  # 等待50毫秒
    
root.mainloop()
