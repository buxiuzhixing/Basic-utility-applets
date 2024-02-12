import tkinter as tk
import random as r
import time as t
import os as o
# 创建主窗口
print("开始构建窗口……")
root=tk.Tk()
root.title("抽学号")
root.geometry('500x400')
root.resizable(0,0)
# 创建一个标签
print("开始构建标签……")
label=tk.Label(root, text="从1到45抽取\n幸运儿",font=("Helvetica",67))
label.pack()
# 创建一个生成随机数的函数
print("开始构建函数……")
def generate_number():
    number=r.randint(1,45)
    label.config(text=str(number),font=("timesnewroman",155))
    print("编号:" + str(number))
    root.title("幸运观众："+ str(number))
def delete():
    o.system("cls")
def about():
    print("="*128,"\n关于：本程序基本框架由ChatGPT生成，使用Python编写\n算法实现：本程序随机数是使用Python原生库Ramdom通过特定的算法生成的。\n请注意：完全的随机性是不存在于世上的。若您对结果存在质疑或不满，那纯属正常。\n\n下载最新版：\n码云：https://gitee.com/seedream7649/basic-utility-applet\nGitHub：https://github.com/buxiuzhixing/basic-utility-applet\n","="*128)
# 创建一个按钮
print("开始创建一个按钮……")
button=tk.Button(root, text="抽取",font=("Helvetica",20), command=generate_number)
button1=tk.Button(root, text="清空记录",font=("Helvetica",20), command=delete)
button2=tk.Button(root, text="关于",font=("Helvetica",20), command=about)
button.pack(),button1.pack(side=tk.LEFT),button2.pack(side=tk.RIGHT)
# 运行主循环
print("运行主循环……\n完成！")
print("="*128)
root.mainloop()
