from tkinter import*

window = Tk()
window.geometry("400x400")
window.config(bg="navy")

def display():
    if (x.get()==1):
        window.config(bg = "violet")
        print(x.get())
    else:
        window.config(bg = "yellow")
        print(x.get())

x = IntVar()
check_button = Checkbutton(window,text = "click",
bg = "peru",padx = 5, pady = 5,onvalue = 1,
offvalue = 0, command = display,variable = x)
check_button.place(x=20,y=20)

window.mainloop()
