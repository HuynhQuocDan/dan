from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("CHECK OUT PAPER")
window.geometry("1900x500")
window.resizable(0,0)

def take_info():
    input = entry.get()
    try:
        if input != "":
            lbl5.config(text = "The booth number " + str(input) + " confirmed")
        else:
            lbl5.config(text = "")
            msb = messagebox.showwarning("Caution","Don't leave this box blank")
    except:
        msb = messagebox.showwarning("Caution","Don't leave this box blank")


font_name = "arial 25 bold"

align_x = 50
align_y = 50
align_step = 100

lbl1 = Label(window,text = "Step 1: Collect the paper in tray 2",font = font_name)
lbl1.place(x=align_x, y=align_y)
lbl2 = Label(window,text = "Step 2: Fill and sign the paper",font = font_name)
lbl2.place(x=align_x, y=align_y + align_step)
lbl3 = Label(window,text = "Step 3: Put the paper to the mailbox 3",font = font_name)
lbl3.place(x=align_x, y=align_y + 2*align_step)
lbl4 = Label(window,text = "Step 4: Confirm your booth information =>",font = font_name)
lbl4.place(x=align_x, y=align_y + 3*align_step)

align_button = 900

lbl5 = Label(window,font = font_name)
lbl5.place(x = align_button, y = align_y + 3*align_step)

btn1 = Button(window, text = "Confirm", font = font_name, width = 10, height = 1, command = take_info)
btn1.place(x = align_button, y = align_y + 2*align_step)

input = StringVar()
entry = Entry(window, width = 20,font = font_name,bd = 4, textvariable = input)
entry.place(x = align_button, y = align_y + align_step)

window.mainloop()
