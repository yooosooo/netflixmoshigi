import tkinter as tk
from tkinter import *

def debut():
    print('debut')
    canvas.delete(btnw)  # <-- this removes the window containing the button

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
btn = Button(root, height = 5, width = 10, text='jouer', command=debut)
btnw = canvas.create_window(200, 200, window=btn)  # <- this is the canvas element to delete from the canvas 

root.mainloop()