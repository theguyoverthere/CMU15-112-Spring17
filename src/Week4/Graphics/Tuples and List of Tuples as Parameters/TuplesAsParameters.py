from tkinter import *

def draw(canvas, width, height):
    #Tuples as parameters
    canvas.create_oval((100,50), (300, 150), fill="yellow")
    points = [(50,30),(150,50),(250,30),(150,10)]
    points.append((20 ,100))
    canvas.create_polygon(points, fill="green")
    points.pop()
    canvas.create_polygon(points, fill="red")

def runDrawing(width = 300, height = 300):
    root = Tk()
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    draw(canvas, width, height)
    root.mainloop()

runDrawing(400,400)