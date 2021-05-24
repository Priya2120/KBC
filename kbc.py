from tkinter import*
import tkinter
from tkinter.constants import LEFT
from tkinter.ttk import Button, Frame, Label
from random import randint
root=tkinter.Tk()
root.geometry("1270x627+0+0")
root.title("WEL COME TO KBC")

root.config(bg="black")

leftframe=Frame(root)
leftframe.grid(row=0,column=0)

topframe=Frame(leftframe)
topframe.grid()

buttonframe=Frame(leftframe)
buttonframe.grid(row=2,column=0)


rightframe=Frame(root)
rightframe.grid(row=0,column=1)

img=PhotoImage(file="/home/priya/Downloads/KBC2.png")

lifeline50=Button(topframe,image=img)
lifeline50.grid(row=0,column=0)

rightframe=Frame(root)
rightframe.grid(row=0,column=1)

img=PhotoImage(file="271.4 kB (2,71,361 bytes)/call")

life=Button(topframe,image=img)
life.grid(row=0,column=1)



root.mainloop()
