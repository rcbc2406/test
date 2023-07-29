import tkinter as tk
from datetime import datetime

def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

root = tk.Tk()
root.title("Analog Clock")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

clock_label = tk.Label(root)
clock_label.pack()

clock_frame = tk.Frame(canvas, bg='white', width=200, height=200)
clock_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

canvas.create_oval(50, 50, 350, 350, width=3)

for i in range(1, 13):
    angle = i * 30 * 3.14159 / 180
    x = 200 + 150 * 0.8 * math.sin(angle)
    y = 200 - 150 * 0.8 * math.cos(angle)
    canvas.create_text(x, y, text=str(i), font=("Helvetica", 12))

hour_hand = canvas.create_line(200, 200, 200, 130, width=5)
minute_hand = canvas.create_line(200, 200, 250, 200, width=3)
second_hand = canvas.create_line(200, 200, 200, 70, width=1)

update_clock()

root.mainloop()
