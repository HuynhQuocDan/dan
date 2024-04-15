from tkinter import*

window = Tk()

def click(a):
    #pass # bỏ qua
    lbl = Label(window,text = "stop" + str(a))
    lbl.pack()
   

window.geometry("400x400+300+200")
btn = Button(window, text = "click", bg = "lime", fg = "white",font ="arial 15 bold",command = Lambda click(234))
btn.pack()

window.mainloop()