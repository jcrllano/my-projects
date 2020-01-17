import tkinter as tk
from googletrans import Translator
import pyttsx3
from tkinter import filedialog
from tkinter import *
from docx import Document
import os

# set the window frame and title
lang = tk.Tk()
lang.title('Boty Translator')
lang.geometry('280x400')

# upload docx document
def load():
    filename = filedialog.askopenfilename()
    documentfile = Document(filename)
    for t in documentfile.paragraphs:
        return(t.text)

# define the function to create the translation
def LangTrans():
    engine = pyttsx3.init()
    translation = Translator(service_urls=['translate.google.com'])
    translation2 = translation.translate(load(), dest='es')
    engine.say(translation2.text)
    engine.runAndWait()
    return translation2.text


# set the labels and buttons
label = tk.Label(lang, text="Click On The Button To Upload File ")
label.grid(row=0, column=2, sticky='w', ipady=1)


button = tk.Button(lang, text="Translate Document", command=LangTrans)
button.grid(row=2, column=2)

lang.update()
lang.mainloop()
