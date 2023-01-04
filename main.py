from tkinter import * 
from tkinter import ttk 

Window = Tk() #Creates new Window
Window.geometry("360x540") #Width x Height 
Window.title("Calculator") #Window's title
icon = PhotoImage(file='calculator.png')
Window.iconphoto(True,icon)
Window.config(background="black")

e = Entry(Window, width = 360 , bg ="Black", fg="white")
e.pack()

def lightMode():
    Window.config(background="white")
    

def equalbutton():
    label = Label(Window, text=e.get(),fg='white',bg='black',activeforeground='white',activebackground='black',bd=0)
    label.pack()


button = Button(Window,text="Mode",command=lightMode,font=('comic sans',10),
                fg='white',bg='black',activeforeground='white',activebackground='black',bd=0)
button.pack()
equal = Button(Window, text="=", command=equalbutton,fg='white',bg='black',activeforeground='white',activebackground='black',bd=0)
equal.pack()
Window.mainloop() #Listen for events and display our window


