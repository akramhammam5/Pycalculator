from tkinter import * 
from tkinter import ttk 

Window = Tk() #Creates new Window
Window.geometry("360x540") #Width x Height 
Window.title("Calculator") #Window's title
icon = PhotoImage(file='calculator.png')
Window.iconphoto(True,icon)
Window.config(background="black")

def appMode():
    Window.config(background="white")


button = Button(Window,text="Light mode",command=appMode,font=('comic sans',10),fg='white',bg='black',activeforeground='white',activebackground='black',bd=0)
button.pack()

Window.mainloop() #Listen for events and display our window


