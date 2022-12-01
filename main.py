from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('800x626')
root.title('Dictionary')
root.configure(bg='#08101c')
root.resizable(0,0)
title = Label(root, text='Rozan Dictionary',font=('Century Schoolbook L','30','bold'),fg='#ffffff',bg='#08101c')
title.place(x=230,y=0)

EnterWord = Label(root, text='Enter the word you want to translate',font=('Liberation Sans Narrow','16',),fg='#ffffff', bg='#08101c')
EnterWord.place(x=260,y=90)

entry = Entry(root, width=50, font=('Liberation Sans Narrow', '14'), fg='Black', bg='Whitesmoke', justify=CENTER, relief=GROOVE)
entry.place(x=170,y=160)
entry.focus_set()

SubmitButton = Button(root, text='Submit', bd=0, bg='#08101c', activebackground='#08103c')
SubmitButton.place(x=364, y=199)

root.mainloop()