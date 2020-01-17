import tkinter as tk
from googletrans import Translator
import pyttsx3
from tkinter import filedialog
from tkinter import *
from docx import Document
import os

lang = tk.Tk()
lang.title('Boty Translator')
lang.geometry('280x400')


def UploadAction():
    filename = filedialog.askopenfilename()
    document = Document(filename)
    for p in document.paragraphs:
        return(p.text)


def LangTrans():
    engine = pyttsx3.init()
    translation = Translator(service_urls=['translate.google.com'])
    translation2 = translation.translate(UploadAction(), dest='en')
    engine.say(translation2.text)
    engine.runAndWait()
    return translation2.text

label = tk.Label(lang, text="Click On The Button To Upload File ")
label.grid(row=0, column=2, sticky='w', ipady=1)


button = tk.Button(lang, text="Translate Document", command=LangTrans)
button.grid(row=2, column=2)

lang.update()
lang.mainloop()
