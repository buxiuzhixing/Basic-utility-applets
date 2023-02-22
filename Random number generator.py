import tkinter as tk
import random
# 创建主窗口
root = tk.Tk()
root.title("随机数生成器")
root.geometry('400x200')
# 创建一个标签
label = tk.Label(root, text="从1到41抽取\n幸运儿",font=("Helvetica",41))
label.pack()
# 创建一个生成随机数的函数
def generate_number():
    number = random.randint(1, 41)
    label.config(text="生成的数字: \n" + str(number))
# 创建一个按钮
button = tk.Button(root, text="生成",font=("Helvetica",17), command=generate_number)
button.pack()
# 运行主循环
root.mainloop()
