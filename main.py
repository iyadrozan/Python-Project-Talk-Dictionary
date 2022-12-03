from tkinter import *
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()

# Function
def Clear():
    entry.delete(0, END)
    entry.config(state=NORMAL)
    TextArea.delete(1.0, END)
    TextArea.config(state=DISABLED)

def Exit():
    res = messagebox.askyesno("Confirm", "Do you want to exit?")
    if res==TRUE:
        root.destroy()
    else:
        pass

def textToSpeech():
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    rete = engine.getProperty('rate')
    engine.setProperty('rate', 180)
    engine.say(entry.get())
    engine.runAndWait()

def textToSpeech1():
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[0].id)
    rete = engine.getProperty('rate')
    engine.setProperty('rate', 180)
    engine.say(TextArea.get("1.0", 'end-1c'))
    engine.runAndWait()

# UI Tkinter
root = Tk()
root.geometry('800x626')
root.title('Dictionary')
root.configure(bg='#08101c')
root.resizable(0,0)
title = Label(root, text='Talk Dictionary',font=('Century Schoolbook L','30','bold'),fg='#ffffff',bg='#08101c')
title.place(x=230,y=0)

EnterWord = Label(root, text='Enter the word you want to translate',font=('Liberation Sans Narrow','16',),fg='#ffffff', bg='#08101c')
EnterWord.place(x=260,y=90)

entry = Entry(root, width=50, font=('Liberation Sans Narrow', '14'), fg='Black', bg='Whitesmoke', justify=CENTER, relief=GROOVE)
entry.place(x=170,y=160)
entry.focus_set()

SubmitButton = Button(root, font='bold', text='Submit', bd=0, bg='#08101c', activebackground='#171D26')
SubmitButton.place(x=310, y=199)

MicButton = Button(root, font='bold', text='Speak', bd=0, bg='#08101c', activebackground='#171D26', command=textToSpeech)
MicButton.place(x=410, y=199)

Meaning = Label(root, text='Meaning', font=('Liberation Sans Narrow','16',), fg='#ffffff', bg='#08101c')
Meaning.place(x=350,y=260)

TextArea = Text(root, font=('Liberation Sans Narrow', '14'), fg='Black', bg='Whitesmoke', width=44, height=7, bd=4, relief=GROOVE, wrap=WORD,)
TextArea.place(x=190,y=290)

ClearBtn = Button(root, font='bold', text='Clear', bd=0, bg='#08101c', activebackground='#171D26', command=Clear )
ClearBtn.place(x=530, y=260)

ExitBtn = Button(root, font='bold', text='Exit', bd=0, bg='#08101c', activebackground='#171D26', command=Exit)
ExitBtn.place(x=410, y=469)

speakBtn = Button(root, font='bold', text='Speak', bd=0, bg='#08101c', activebackground='#171D26', command=textToSpeech1)
speakBtn.place(x=320, y=469)    

root.mainloop()