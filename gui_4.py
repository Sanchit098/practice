import tkinter
from tkinter import *
def new_new():
    v = tkinter.Tk()
    v.geometry("300x700")
    B1=tkinter.Button(v, text="helloji")
    B1.pack()
def new_window():

    w = tkinter.Tk()
    w.geometry("300x700")
    b = tkinter.Button(w,text="Good worok",width = 14, height = 2,command = new_new)
    b.pack()
def __mina():
    main = tkinter.Tk()
    main.title("Hello Everyone")
    main.geometry("360x400")
    button = tkinter.Button(main,text="hello",width =25, command=new_window)
    button.pack()
    #

    main.mainloop()
__mina()

# from tkinter import *
# master = Tk()
# Label(master, text='First Name').grid(row=0)
# Label(master, text='Last Name').grid(row=1)
# e1 = Entry(master)
# e2 = Entry(master)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# mainloop()
# s= Canvas(main, width = 40 ,height=60)
# s.pack()
# Label(main,text="firstname").grid(row=0)
# Label(main,text="Last Name").grid(row=1)
# e1 = Entry(main).grid(row=0,column=1)
# e2 = Entry(main).grid(row=1,column=1)
# e1.pack()
# e2.pack()