from tkinter import * 
from tkinter import ttk 

Window = Tk() #Creates new Window
Window.geometry("360x540") #Width x Height 
Window.title("Calculator") #Window's title
icon = PhotoImage(file='calculator.png')
Window.iconphoto(True,icon)
Window.config(background="black")

def clickZero():
    print("0")

button = Button(Window,text="0",command=clickZero,font=('comic sans',30),fg='white',bg='black',activeforeground='white',activebackground='black')
button.pack()

Window.mainloop() #Listen for events and display our window


