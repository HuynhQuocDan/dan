from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer")
root.iconbitmap("D:\Learn\last semester\Interface\dollar.ico")

my_img1 = ImageTk.PhotoImage(Image.open("images/number1.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/number2.png"))
my_img3 = ImageTk.PhotoImage(Image.open("images/number3.png"))
my_img4 = ImageTk.PhotoImage(Image.open("images/number4.png"))

image_list = [my_img1, my_img2, my_img3, my_img4]

my_label = Button(image = image_list[0])
my_label.grid(row = 0, column = 0, columnspan = 3)

def next(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number])
    my_label.grid(row = 0, column = 0, columnspan = 3)

    button_next = Button(root, text = ">>", command = lambda: next(image_number + 1))
    button_next.grid(row = 1, column = 2)

    if image_number == len(image_list) - 1:
        button_next = Button(root, text = ">>", state = DISABLED)
        button_next.grid(row = 1, column = 2)

def back(image_number):
    global my_label
    global button_next
    global button_back

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number])
    my_label.grid(row = 0, column = 0, columnspan = 3)

    button_back = Button(root, text = "<<", command = lambda: back(image_number - 1))
    button_back.grid(row = 1, column = 0)
    if image_number <= 0:
        button_back = Button(root, text = "<<", state = DISABLED)
        button_back.grid(row = 1, column = 0)

button_back = Button(root, text = "<<", command = lambda: back(0))
button_next = Button(root, text = ">>", command = lambda: next(1))
button_exit = Button(root, text = "EXIT", command = root.quit)

button_back.grid(row = 1, column = 0)
button_exit.grid(row = 1, column = 1)
button_next.grid(row = 1, column = 2)

root.mainloop()