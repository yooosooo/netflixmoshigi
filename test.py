from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import pandas as pd
import openpyxl


root = Tk()
root.title("baba")
root.geometry("400x400")

root.resizable(False, False)

FILENAME = 'images\ggggg.png'
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

tk_img = ImageTk.PhotoImage(Image.open(FILENAME))
canvas.create_image(10, 10, anchor = NW, image=tk_img)

#creating a Label widget
myLabel = Label(canvas, text="Do you know this word?")
#shoving in onto the screen
myLabel.pack()


bblabel = Label(root, text="", bg="green", fg="white")
bblabel.pack()

cclabel = Label(root, text="")
cclabel.pack()

   
btn1 = Button(root, text="Yes", command = next, anchor = 'w',
                    width = 5, activebackground = "#33B5E5")
btn1_window = canvas.create_window(10, 10, anchor='nw', window=btn1)

btn2 = Button(root, text="No", anchor='w',
                    width = 10, activebackground = "#33B5E5")
btn2_window = canvas.create_window(10, 10, anchor='e', window=btn2)

exit_button = Button(root, text='Exit')
exit_button.pack(fill=tk.X, pady=5)

btn11 = Button(root, text='Next')






root.mainloop()