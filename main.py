from tkinter import * 
from tkinter import ttk 

Window = Tk() #Creates new Window
Window.geometry("360x540") #Width x Height 
Window.title("Calculator") #Window's title
icon = PhotoImage(file='calculator.png')
Window.iconphoto(True,icon)
Window.config(background="black")

Window.mainloop() #Listen for events


