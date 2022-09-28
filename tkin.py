
from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import pandas as pd
import openpyxl

i=0
global current_word
BACKGROUND_COLOR = "#B1B2DD"

list1 = ["hey", "bye", "hi", "la","-e"]
mist = ["a", "b", "c", "d", "e"]
bin1 = []
bin2 = []

current_word = list1[0]

def dormamu():
    btn11.pack_forget()
    exit_button.pack_forget()
    btn1.pack(fill=tk.X, pady=5)
    btn2.pack(fill=tk.X, pady=5) 
    exit_button.pack(fill=tk.X, pady=5)

def next():
    global current_word
    global current_sent
    count = len(list1)
    
    global i
    
    if (i < count):
        current_word = list1[i]
        current_sent = mist[i]
        
        bblabel.config(text=current_word)
        cclabel.config(text="Location:" + "\n" + current_sent)
        i = i+1
    else:
        btn1.pack_forget()
        btn2.pack_forget()

        myLabel.config(text="finished")
        
def search():
    btn1.pack_forget()
    btn2.pack_forget()
    exit_button.pack_forget()
    btn11.pack(fill=tk.X, pady=5)
    exit_button.pack(fill=tk.X, pady=5)

    global current_word
    
    url = 'https://www.merriam-webster.com/dictionary/' + current_word
    webbrowser.open(url, new=0)
   
def throw():
    global current_word
    global current_sent

    bin1.append(current_word)
    bin2.append(current_sent)

    # print(bin1)
    # print(bin2)

def convcel():
    global bin1
    global bin2

    df = pd.DataFrame({'Word': [*bin1], 'Sent': [*bin2]})
    #df = pd.DataFrame([bin1], [bin2], columns=['word', 'sentence'])
    #df.to_excel('pandas_to_excel_no_index_header.xlsx', index=False, header=False)
    
    writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()

    print(writer)
    print(df)

#-----------------GUI part------------------

# import ImageTk

root = Tk()
root.title("baba")
root.geometry("400x400")

root.resizable(False, False)

FILENAME = 'images\ggggg.png'
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
tk_img = PhotoImage(file = "images\ggggg.png")
canvas1 = Canvas(root, width = 400, height = 400)
canvas1.pack(fill = "both", expand = True)
canvas1.create_image( 0, 0, image = tk_img, 
                     anchor = "nw")

#creating a Label widget
myLabel = Label(root, text="Do you know this word?")
#shoving in onto the screen
myLabel.pack()


bblabel = Label(root, text="", bg="green", fg="white")
bblabel.pack()

cclabel = Label(root, text="")
cclabel.pack()

   
btn1 = Button(root, text="Yes", command = next, anchor = 'w',
                    width = 5, activebackground = "#33B5E5")
btn1_window = canvas.create_window(10, 10, anchor='nw', window=btn1)

btn2 = Button(root, text="No", command=lambda: [search(), throw()], anchor='e',
                    width =10)
btn2_window = canvas.create_window(10, 10, anchor='e', window=btn2)

exit_button = Button(root, text='Exit', command=lambda: [root.quit(), convcel()])
exit_button.pack(fill=tk.X, pady=5)

btn11 = Button(root, text='Next', command=lambda: [next(), dormamu()])



next()

root.mainloop()