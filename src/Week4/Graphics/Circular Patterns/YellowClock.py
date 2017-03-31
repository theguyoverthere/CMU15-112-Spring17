import math
from tkinter import*

def draw(canvas, width, height):
    cx, cy, r = width/2, height/2, min(width, height) / 3
    canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="yellow")

    #make smaller so time labels lie inside clock
    r *= 0.85

    for hour in range(12):
        hourAngle = (math.pi / 2) -  (2 * math.pi) * (hour / 12)
        hourX = cx + r * math.cos(hourAngle)
        hourY = cy - r * math.sin(hourAngle)

        label = str(hour if (hour > 0) else 12)
        canvas.create_text(hourX, hourY, text=label, font="Arial")

def runDrawing(width=400, height=400):
    root =Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()

runDrawing(400, 200)