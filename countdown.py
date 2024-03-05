import tkinter as tk
from tkinter import messagebox

class CountdownApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Countdown Timer")
        
        self.label = tk.Label(self, font=("Helvetica", 16))
        self.label.pack(pady=10)
        
        self.time_entry = tk.Entry(self, font=("Helvetica", 16))
        self.time_entry.pack(pady=10)
        
        self.start_button = tk.Button(self, text="Mulai Countdown", command=self.start_countdown)
        self.start_button.pack(pady=10)


    def start_countdown(self):
        self.countdown(timer = int(self.time_entry.get()))


    def countdown(self, timer):
        if timer > 0:
            timer -= 1
            self.label.config(text="Waktu tersisa: {} detik".format(timer))
            self.label.after(1000, self.countdown, timer) # time in ms

        else:
            self.label.config(text="Waktu habis!")
            messagebox.showinfo("Countdown Selesai", "Waktu countdown telah habis!")

if __name__ == "__main__":
    app = CountdownApp()
    app.mainloop()
