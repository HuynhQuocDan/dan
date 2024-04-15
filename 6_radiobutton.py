from tkinter import *
window = Tk()
window.geometry("300x300")
def order():
    if(x.get())==0:
        lbl.config(text = "ban chon cam")
    elif (x.get())==1:
        lbl.config(text = "ban chon quyt")
    elif (x.get())==2:
        lbl.config(text = "ban chon mit")
    elif (x.get())==3:
        lbl.config(text = "ban chon dua")
fruit = ["cam","quyt","mit","dua"]

lbl = Label(window, text = "")
lbl.pack()
x = IntVar()
x.set(1)
lbl.config(text = "ban chon quyt")
for index in range(len(fruit)):
    radio = Radiobutton(window,text = fruit[index],
    value = index, variable = x, command = order)
    radio.pack(anchor=W)

window.mainloop()