from tkinter import *

window = Tk()
window.title("hocgioi")
window.geometry("400x400+300+200")
window.iconbitmap("D:\Learn\last semester\Interface\gear.ico")
window.config(background = "orange")

photo = PhotoImage(file = "D:\Learn\last semester\Interface\doraemon.png")

lbl = Label(window, text = "Hello",font = "arial 20 bold",bg = "white", fg = "Green", image = photo)
#lbl.place(x = 30, y = 20) #định vị tọa độ
lbl.pack() #định vị theo căn lề giữa
#lbl.grid(row = 0, column = 2) #định vị ma trận lưới

window.mainloop()
