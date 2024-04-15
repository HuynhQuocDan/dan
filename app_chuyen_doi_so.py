from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Number Convert")
window.geometry("310x225")
window.resizable(0,0)

def convert():
    input = entry.get()
    try:
        if int(input)>0:
            bin_cv = bin(int(input))
            lbl3.config(text = "Bin:  " + str(bin_cv))

            hex_cv = hex(int(input))
            lbl1.config(text = "Hex:  " + str(hex_cv))

            oct_cv = oct(int(input))
            lbl2.config(text = "Oct:  " + str(oct_cv))

        else:
            msb = messagebox.showwarning("Canh bao","hay nhap vao 1 so nguyen duong")
    except:
        msb = messagebox.showwarning("Canh bao","khong de trong o nay")

def backspace():
    a = entry.get()
    a = a[:-1]
    input.set(a)
def expand():
    window.geometry("500x500")
def contract():
    window.geometry("310x225")

lbl1 = Label(window,text = "Hex:")
lbl1.place(x=20, y=20)
lbl2 = Label(window,text = "Oct:")
lbl2.place(x=20, y=60)
lbl3 = Label(window,text = "Bin:")
lbl3.place(x=20, y=100)

btn1 = Button(window, text = "Convert", width = 7,command = convert)
btn1.place(x=20, y=180)
btn2 = Button(window, text = "Backspace", width = 7, command = backspace)
btn2.place(x=90, y=180)
btn3 = Button(window, text = "Expand", width = 7, command = expand)
btn3.place(x=160, y=180)
btn4 = Button(window, text = "Contract", width = 7, command = contract)
btn4.place(x=230, y=180)

input = StringVar()
entry = Entry(window,width = 43, textvariable = input)
entry.place(x = 20, y = 140)

window.mainloop()