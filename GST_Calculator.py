from tkinter import *

root = Tk()
root.title("sagnik's GST calculator")
root.iconbitmap(r'C:\Users\User\Desktop\calc.ico')


e = Entry(root, width=35,borderwidth=5, bg="black", fg="white")
e.grid(row=0, column=0,columnspan=3,padx=5,pady=5)
#e.insert(0,"")

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# clear oparation 

def button_clear():
    e.delete(0, END)

# mathematical oparation

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)
def button_substract():
    first_number = e.get()
    global f_num
    global math
    math = "substraction"
    f_num = int(first_number)
    e.delete(0, END)
def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)
def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "divition"
    f_num = int(first_number)
    e.delete(0, END)

# gst calculation

def button_gst():
    first_number = e.get()
    global f_num
    global math
    math = "GST"
    f_num = int(first_number)
    e.delete(0, END)

# equal oparation

def button_equal():
    second_number = e.get()
    e.delete(0,END)

    if (math=="addition"):
        e.insert(0, f_num + int(second_number))
    if (math=="substraction"):
        e.insert(0, f_num - int(second_number))
    if (math=="multiplication"):
        e.insert(0, f_num * int(second_number))
    if (math=="divition"):
        e.insert(0, f_num / int(second_number))
    if (math=="GST"):
        e.insert(0, f_num + f_num*(int(second_number)/100))

# buttons

button_1 = Button(root, text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2 = Button(root, text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3 = Button(root, text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4 = Button(root, text="4",padx=40,pady=20,command=lambda: button_click(4))
button_5 = Button(root, text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6 = Button(root, text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7 = Button(root, text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8 = Button(root, text="8",padx=40,pady=20,command=lambda: button_click(8))
button_9 = Button(root, text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0 = Button(root, text="0",padx=40,pady=20,command=lambda: button_click(0))

button_add = Button(root, text="+",padx=40,pady=20,command=button_add)
button_substract = Button(root, text="-",padx=40,pady=20,command=button_substract)
button_multiply = Button(root, text="*",padx=40,pady=20,command=button_multiply)
button_divide = Button(root, text="/",padx=40,pady=20,command=button_divide)
button_gst = Button(root, text="GST",padx=40,pady=20,bg="#0362fc",command=button_gst)

button_clear = Button(root, text="C",bg="#fcdf03",fg="black",padx=80,pady=20,command=button_clear)
button_equal = Button(root, text="=",bg="#03fcca",fg="black",padx=80,pady=20,command=button_equal)
button_exit = Button(root, text="Exit",bg="#ff3333",fg="white",padx=40,pady=20,command=root.quit)

# grids

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_clear.grid(row=4,column=1,columnspan=2)
button_equal.grid(row=5,column=1,columnspan=2)

button_add.grid(row=5,column=0)
button_substract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)
button_gst.grid(row=7,column=0)

button_exit.grid(row=7,column=1)

root.mainloop()
