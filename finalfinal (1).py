from array import array
import nltk
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random

import re
nltk.download('all')
nltk.download('punkt')
nltk.download('wordnet')
global ray
global Senray

file = 'tesss.txt'

ray = []
Senray = []

with open(file, 'r') as f:
    content = f.readlines()
    #print(content)

for line in content:
    sentence = line

    cleaned_content = re.sub(r'[^\.\?\!\w\d\s]','',sentence)
    #print(cleaned_content)

    cleaned_content = cleaned_content.lower()

    word_tokens = nltk.word_tokenize(cleaned_content)
    #print(word_tokens)

    tokens_pos = nltk.pos_tag(word_tokens)
    #print(tokens_pos)

    from nltk.corpus import wordnet

    def get_wordnet_pos(word):
        """Map POS tag to first character lemmatize() accepts"""
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)

    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in word_tokens]

    #print(lemmatized_words)

    stopwords_list = stopwords.words('english')

    unique_words = set(lemmatized_words)
    final_words = lemmatized_words
    for word in unique_words:
        if word in stopwords_list:
            while word in final_words: final_words.remove(word)

    #print(final_words)

    def remove_punc(string):
        punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''
        for ele in string:  
            if ele in punc:  
                string = string.replace(ele, "") 
        return string
    
    lis = [remove_punc(i) for i in final_words]
    #print(lis) 
    
    str_list = list(filter(None, lis))
    #print(str_list)

    strr_list = [*set(str_list)]

    import pandas as pd

    df = pd.read_excel (r'Book1.xlsx') #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
    mylist = df['abandon'].tolist()


    #print (mylist)


    for l1 in strr_list:
        for l2 in mylist:
            if l1 == l2:
                ray.append(l1)
                Senray.append(sentence)
    result = list(set(ray))
# print(ray)
# print(Senray)



#---------------tkinter part---------------------------------------

from tkinter import *
import tkinter as tk
from tkinter import ttk
import webbrowser
import pandas as pd
import openpyxl

i=0
global current_word


# list1 = ["hey", "bye", "hi", "la","-e"]
# mist = ["a", "b", "c", "d", "e"]
bin1 = []
bin2 = []

current_word = ray[0]

def dormamu():
    btn11.pack_forget()
    exit_button.pack_forget()
    btn1.pack(fill=tk.X, pady=5)
    btn2.pack(fill=tk.X, pady=5) 
    exit_button.pack(fill=tk.X, pady=5)

def next():
    global current_word
    global current_sent
    count = len(ray)
    
    global i
    
    if (i < count):
        current_word = ray[i]
        current_sent = Senray[i]
        
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

    #print(writer)
    #print(df)

root = Tk()
root.title("baba")
root.geometry("400x400+300+100")

root.resizable(False, False)

#creating a Label widget
myLabel = Label(root, text="Do you know this word?")
#shoving in onto the screen
myLabel.pack()


bblabel = Label(root, text="", bg="green", fg="white")
bblabel.pack()

cclabel = Label(root, text="")
cclabel.pack()

   
btn1 = Button(root, text="Yes", command = next)
btn1.pack(fill=tk.X, pady=5)

btn2 = Button(root, text="No", command=lambda: [search(), throw()])
btn2.pack(fill=tk.X, pady=5)

exit_button = Button(root, text='Exit', command=lambda: [root.quit(), convcel()])
exit_button.pack(fill=tk.X, pady=5)

btn11 = Button(root, text='Next', command=lambda: [next(), dormamu()])

next()

root.mainloop()



