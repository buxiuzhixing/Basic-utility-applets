import tkinter as tk  
from tkinter import messagebox  
  
class CountdownTimer:  
    def __init__(self, master=None):  
        self.master = master  
        self.remaining_time = 0  
        self.countdown_seconds = 60  # 默认的倒计时时间  
        self.running = False  
        self.paused = False  
        self.create_widgets()  
  
    def create_widgets(self):  
        self.label = tk.Label(self.master, text=str(self.countdown_seconds), font=('Helvetica', 24))  
        self.label.pack()  
  
        self.entry = tk.Entry(self.master, justify='center')  
        self.entry.insert(0, str(self.countdown_seconds))  # 预设默认时间  
        self.entry.pack()  
  
        self.set_button = tk.Button(self.master, text="Set Time", command=self.set_countdown_time, state='normal')  
        self.set_button.pack()  
  
        self.start_button = tk.Button(self.master, text="Start", command=self.start_countdown, state='normal')  
        self.start_button.pack()  
  
        self.pause_button = tk.Button(self.master, text="Pause", command=self.pause_countdown, state='disabled')  
        self.pause_button.pack()  
  
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_countdown)  
        self.reset_button.pack()  
  
        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.quit)  
        self.quit_button.pack()  
  
    def set_countdown_time(self):  
        if not self.running:  
            try:  
                self.countdown_seconds = int(self.entry.get())  
                if self.countdown_seconds < 0:  
                    self.countdown_seconds = 0  
                self.label.config(text=str(self.countdown_seconds))  
                self.start_button.config(state='normal')  
                self.pause_button.config(state='disabled')  
            except ValueError:  
                messagebox.showerror("Error", "Please enter a valid number.")  
  
    def start_countdown(self):  
        if not self.running and not self.paused:  
            self.running = True  
            self.paused = False  
            self.start_button.config(state='disabled')  
            self.pause_button.config(state='normal')  
            self.countdown(self.countdown_seconds)  
  
    def countdown(self, remaining_time):  
        self.remaining_time = remaining_time  
        if self.remaining_time >= 0:  
            mins, secs = divmod(self.remaining_time, 60)  
            timer = '{:02d}:{:02d}'.format(mins, secs)  
            self.label.config(text=timer)  
            if self.running:  
                self.master.after(1000, self.countdown, self.remaining_time - 1)  
        else:  
            self.label.config(text="Time's up!")  
            self.reset_countdown()  
  
    def pause_countdown(self):  
        if self.running:  
            self.paused = True  
            self.running = False  
            self.start_button.config(text="Resume", command=self.resume_countdown)  
            self.pause_button.config(state='disabled')  
  
    def resume_countdown(self):  
        if self.paused:  
            self.paused = False  
            self.running = True  
            self.start_button.config(text="Start", command=self.start_countdown, state='disabled')  
            self.pause_button.config(state='normal')  
            self.countdown(self.remaining_time)  
  
    def reset_countdown(self):  
        self.running = False  
        self.paused = False  
        self.remaining_time = self.countdown_seconds  
        self.label.config(text=str(self.countdown_seconds))  
        self.start_button.config(text="Start", command=self.start_countdown, state='normal')  
        self.pause_button.config(state='disabled')  
  
if __name__ == '__main__':  
    root = tk.Tk()  
    root.title("Countdown Timer")  
    app = CountdownTimer(master=root)  
    root.mainloop()
