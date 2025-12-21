import tkinter as tk
from tkinter import messagebox
import random

# 创建主窗口
root = tk.Tk()
root.title("抽学号")
root.geometry('500x300')
root.resizable(0, 0)

# 界面元素样式配置
INITIAL_TEXT = "从1到45抽取\n幸运儿"
INITIAL_FONT = ("Helvetica", 50)
RESULT_FONT = ("Arial", 120)
BUTTON_FONT = ("Microsoft YaHei", 14)

# 创建主标签
label = tk.Label(root, text=INITIAL_TEXT, font=INITIAL_FONT, wraplength=450)
label.pack(pady=20)

# 按钮功能实现
def generate_number():
    """生成随机数并更新界面"""
    number = random.randint(1, 45)
    label.config(text=str(number), font=RESULT_FONT)
    root.title(f"幸运观众：{number}")

def reset_interface():
    """重置界面到初始状态"""
    label.config(text=INITIAL_TEXT, font=INITIAL_FONT)
    root.title("抽学号")

def show_about():
    """显示关于信息"""
    about_content = """
    版本：R1 优化特别版
    功能：随机抽取学号
    
    开发信息：
    - V1-V2.5最终纪念版 由 ChatGPT(GPT-3.5) 生成，DeepSeek 改良发布 R1 优化特别版
    - 使用 Python 3.x 开发
    - 随机算法：Python 标准库 random 模块
    
    注意事项：
    1. 理论上每次抽取概率均等
    2. 允许重复抽取机制设计
    3. 界面数据可通过[清空]按钮重置
    
    项目地址：
    码云：https://gitee.com/seedream7649/basic-utility-applet
    GitHub：https://github.com/buxiuzhixing/Basic-utility-applets
    """
    messagebox.showinfo("关于本程序", about_content)

# 按钮容器框架
button_frame = tk.Frame(root)
button_frame.pack(side=tk.BOTTOM, pady=15)

# 创建功能按钮
btn_style = {'font': BUTTON_FONT, 'height': 1, 'width': 8}

tk.Button(button_frame, text="抽 取", **btn_style, 
         command=generate_number, bg='#4CAF50').pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="清 空", **btn_style,
         command=reset_interface, bg='#f44336').pack(side=tk.LEFT, padx=10)
tk.Button(button_frame, text="关 于", **btn_style,
         command=show_about, bg='#2196F3').pack(side=tk.LEFT, padx=10)

# 运行主循环
root.mainloop()
