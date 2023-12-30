﻿import tkinter as tk
import random
import time as t
# 创建主窗口
print("开始构建窗口……")
root = tk.Tk()
root.title("抽学号")
root.geometry('500x300')
# 创建一个标签
print("开始构建标签……")
label = tk.Label(root, text="从1到45抽取\n幸运儿",font=("Helvetica",67))
label.pack()
# 创建一个生成随机数的函数
print("开始构建生成随机数的函数……")
def generate_number():
    number = random.randint(1,45)
    label.config(text=str(number),font=("timesnewroman",155))
    print("编号:" + str(number))
    root.title("幸运观众："+ str(number))
# 创建一个按钮
print("开始创建一个按钮……")
button = tk.Button(root, text="抽取",font=("Helvetica",20), command=generate_number)
button.pack()
la = tk.Label(root, text="2023 ©ChatGPT\nMade with Python",font=("timesnewroman",8))
la.pack()
# 运行主循环
print("运行主循环……\n完成！\n===========================================")
root.mainloop()
