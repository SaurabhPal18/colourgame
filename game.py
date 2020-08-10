from tkinter import *
from tkinter import messagebox
import random
from random import randint

global count,count1
count=0
count1=0

master= Tk()

canvas_width =400
canvas_height=400

w=Canvas(master,width=canvas_width,height=canvas_height)

w.pack()

def myone():
    global count1,count
    r=20

    for i in range(60):
        colors=["red","green","blue","pink","orange"]
        colorchoice=random.choice(colors)
        if colorchoice== "red":
            count=count+1
        if colorchoice== "green":
            count1=count1+1
        x=randint(0+r,400-r)
        y=randint(0+r,400-r)
        w.create_oval(x-r,y-r,x+r,y+r,fill=colorchoice)
    
    waithere()
    ans="No.of red balls is ",count,"No.of Blue Balls is",count1
    messagebox.showinfo("Your ans is",ans)
def waithere():
    var=IntVar()
    master.after(9000,var.set,1)
    master.wait_variable(var)
   
b=Button(master,text="start",bg="#e79700",width=15,height=1,fg="White",command=myone)
b.pack()

mainloop()    
